第一步：安装tensorflow和tensorflow model，过于基础不在叙述。

第二步：使用LabelImg自定义数据集

2.1 下载labelImg https://github.com/tzutalin/labelImg

2.2 使用labelImg制作数据集

2.3 使用代码xml_to_csv.py将所有xml统一到一个文件中

2.4 使用代码generate_tfrecord.py将csv转为tfRecord文件

第三步：配置训练文件和模型

3.1 在..\object_detection\samples\configs下拷贝一个配置信息到..\object_detection\my training

例如拷贝ssd_mobilenet_v1_coco.config文件

修改：
9行num_classes、141batch_size、173行训练数据路径、187行测试数据路径
删除：fine_tune_checkpoint: "PATH_TO_BE_CONFIGURED/model.ckpt" 和from_detection_checkpoint: true
3.2 
