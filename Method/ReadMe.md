第一步：安装tensorflow和tensorflow model，过于基础不在叙述。

第二步：使用LabelImg自定义数据集

2.1 下载labelImg https://github.com/tzutalin/labelImg
2.2 使用labelImg制作数据集
2.3 使用代码xml_to_csv.py将所有xml统一到一个文件中
2.4 使用代码generate_tfrecord.py将csv转为tfRecord文件
