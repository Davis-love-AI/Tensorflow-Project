第一步：安装 tensorflow 和 tensorflow model <br>
1.1 安装 tensorflow-gpu、下载 tensorflow-models 并解压 <br>
1.2 配置 protoc <br>
  在 https://github.com/google/protobuf/releases 中选择windows版本，解压后将bin文件夹下的 protoc.exe 放在 C:\Windows 下。<br>
  在 models\research\ 目录下打开命令行窗口，输入：protoc object_detection/protos/*.proto --python_out=.<br>
1.3 配置 COCO API<br>
  查看文件Pycocotools安装方法.zip<br>
1.4 配置windows环境变量 <br>
  pythonpath C:\Tensorflow\models\research<br>
  pythonpath C:\Tensorflow\models\research\slim

#第二步：使用LabelImg自定义数据集<br>
2.1 下载 labelImg https://github.com/tzutalin/labelImg<br>
2.2 使用 labelImg 制作数据集<br>
2.3 使用代码 xml_to_csv.py 将所有xml统一到一个文件中<br>
2.4 使用代码 generate_tfrecord.py 将csv转为tfRecord文件

#第三步：配置训练文件和模型<br>
3.1 在..\object_detection\samples\configs下拷贝一个配置信息到..\object_detection\training<br>
例如拷贝ssd_mobilenet_v1_coco.config文件<br>
修改：<br>
9行num_classes、141batch_size、173行训练数据路径、187行测试数据路径<br>
删除：fine_tune_checkpoint: "PATH_TO_BE_CONFIGURED/model.ckpt" 和from_detection_checkpoint: true<br>
3.2 

第四步：训练模型<br>
目前版本(tensorflow 1.12)使用代码为：<br>
python model_main.py --model_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_coco.config

第五步 移植安卓端<br>
Android Studio版本 3.0.2
报错：Could not find com.android.tools.build:gradle:3.0.1.<br>
解决方案：https://majing.io/posts/10000004111202<br>
