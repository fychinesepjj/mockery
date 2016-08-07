#Mocker使用说明
---

##目录
    * 项目说明
    * 代码结构
    * 安装方法
    * 配置说明
    * 搭建教程
        1. 创建项目
        2. 准备数据
        3. 编写Case
        4. 数据请求
        5. 执行用例

##项目说明
　　Mocker的名称源于Mock，英文原意是模仿者的意思，开发Mocker的主要目的是减轻测试者在黑盒测试某些不必要环节的工作量，提高黑盒测试整体运作效率。不同于以往的黑盒测试，Mocker对使用者有一定的编程要求，但又不至于像白盒测试那么高，介于二者之间。
　　Mocker最大的特点是灵活性高，最大不足是覆盖面较窄，主要用途是完成黑盒测试中对API结果的验证。


##代码结构
```
    ---- mocker
        ---- conf
             ---- global_settings.py
        ---- case.py
        ---- color.py
        ---- expect.py
        ---- request.py
        ---- response.py
        ---- utils.py
    ---- exampleProject
        ---- data
             ---- exampleData.py
        ---- case.py
        ---- request.py
        ---- run.py
        ---- settings.py
```

