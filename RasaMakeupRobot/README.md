# 美妆/护肤产品的问答机器人-Labubu

本项目是一个基于rasa实现的美妆/护肤产品问答机器人的项目

## 涵盖内容
 - 美妆/护肤产品的类别，价格
 - 产品使用效果
 - 产品的竞品
 - 集团与品牌的归属关系

## 安装

 在anaconda下配置环境，rasa0.34的最新版本容易出现了一些未知BUG，所以改用之前的0.33或0.32版。
 
    1.创建conda虚拟环境：
        conda create -n rasa python=3.7
    2.切换到虚拟环境rasa下：
        source activate rasa
    3.安装 rasa==0.32.0:
        pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
 
> 注意：因为rasa更新比较快，依赖环境随时会发生变化，建议使用conda的虚拟环境


## 操作流程

 1. 切换到 RasaMakeupRobot 目录下，命令行执行：


    rasa intit  # 初始化 rasa 配置
    rasa x  # 出现rasa可视化对话界面
    
 2. 准备nlu语料库（在RasaMakeupRobot/data/nlu.yml下）
 
 3. 执行 nlu 任务


    nlu任务主要是完成 intent 分类（意图识别） 和 slot词槽 （实体位置）
        rasa train nlu  # 训练nlu模型，训练好的模型会存入 models 中
    
    
TO BE CONTINUE...