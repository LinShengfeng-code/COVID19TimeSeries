# 预测美国未来K天的新冠确诊病例数
```analysis.ipynb``` 中包含了整个预测流程。包括数据预处理、创建数据集、模型训练、预测、模型保存。  
```SourceDataObtain.py``` 是获取数据源并保存到本地的脚本，运行```analysis.ipynb```前需要先运行这个脚本。  
```utils.py``` 是获取最新数据对应日期的脚本，也需要先于```analysis.ipynb```运行。