import numpy as np
import tensorflow as tf
import cv2
import os

from object_detection.utils import visualization_utils as vis_util
from object_detection.utils import label_map_util

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # 这是默认的显示等级，显示所有信息
cv2.setUseOptimized(True)  # 使用多线程加速

# 要改的内容
###############################################
PATH_TO_CKPT = 'model\\ssd_mobilenet_v1_graph.pb'   # 模型及标签地址
PATH_TO_LABELS = 'model\\mscoco_label_map.pbtxt'

NUM_CLASSES = 90  # 检测对象个数

camera_num = 0  # 要打开的摄像头编号，可能是0或1
width, height = 1280, 720  # 视频分辨率
###############################################

# 加载冻结模型到内存中
detection_graph = tf.Graph()  # tf.Graph() 表示实例化了一个类(一个用于 tensorflow 计算和表示用的数据流图)
with detection_graph.as_default():  # .as_default() 表示将这个类实例，也就是新生成的图作为整个 tensorflow 运行环境的默认图
    od_graph_def = tf.GraphDef()  # 新建GraphDef文件，用于临时载入模型中的图
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:  # 获取文本操作句柄
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)  # ParseFromString反序列化
        tf.import_graph_def(od_graph_def, name='')  # 将图形从 graph_def 导入当前的默认 Graph

# 加载标签
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
# 得到类别id与name对应关系的字典

mv = cv2.VideoCapture(camera_num)  # 打开摄像头

mv.set(3, width)     # 设置分辨率
mv.set(4, height)


config = tf.ConfigProto()  # tf.ConfigProto()函数用在创建session的时候，用来对session进行参数配置
config.gpu_options.allow_growth = True
with detection_graph.as_default():
    with tf.Session(graph=detection_graph, config=config) as sess:
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        while True:
            ret, image_source = mv.read()  # 读取视频帧
            image_np = cv2.resize(image_source, (width, height), interpolation=cv2.INTER_CUBIC)
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # 实际检测
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            # 检测结果可视化
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=4)
            cv2.imshow("video", image_np)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出
                break
