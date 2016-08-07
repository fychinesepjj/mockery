#Mocker使用说明
---

##目录
    * 项目说明
    * 项目结构
    * 安装&配置
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
　　为了降低Mocker的使用门槛，加快项目的创建，Mocker引入了一些快捷指令如：`run`，`create`等，让使用者更容易掌握。


##项目结构
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

##安装&配置

###基本运行环境
  * [Python2.7+](https://www.python.org/downloads/)
  * [Python3+](https://www.python.org/downloads/)

###第三方依赖
  * requests >= 2.10.0
  * termcolor >= 1.1.0

  可使用`pip install -r requirements.txt`安装


###Mocker安装方法
  1. 下载安装最新版本[python](https://www.python.org/downloads/)
  2. `git clone xxx` or 直接下载源码gz文件
  3. 打开或解压源码文件夹
  4. 进入./dist目录
  5. 执行安装命令`pip install Mocker-xxx.zip` (此方法会检查第三方依赖，如不存在会自动下载安装)
  6. 打开命令控制台
     * window下执行win+R，输入cmd，进入命令提示符界面
     * linux 可直接打开命令提示符界面
     * 输入`python`命令，执行`import Mocker;Mocker.VERSION`查看安装是否成功
### 其他
  * 需要升级Mocker，可以下载最新版本，同样执行上述安装步骤即可
  * 需要卸载Mocker，执行`pip uninstall Mocker`进行卸载
  * 如果需要Mocker依赖一同卸载，下载`pip install pip-autoremove`, 执行`pip-autoremove Mocker`进行卸载
  * 如有需要Mocker后续会提交pip库，方便下载