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
             ---- __init__.py 
             ---- project_template
        ---- bin
             ---- __init__.py 
             ---- mocker.py  #部署后，命令脚本
        ---- management
             ---- __init__.py
        ---- __init__.py  
        ---- case.py
        ---- color.py
        ---- expect.py
        ---- request.py
        ---- response.py
        ---- utils.py
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

###其他
  * 需要升级Mocker，可以下载最新版本，同样执行上述安装步骤即可
  * 需要卸载Mocker，执行`pip uninstall Mocker`进行卸载
  * 如果需要Mocker依赖一同卸载，下载`pip install pip-autoremove`, 执行`pip-autoremove Mocker`进行卸载
  * 后续Mocker会提交pip库，方便下载


##配置说明
```python
# 调试模式
DEBUG = False

# 网络请求超时最大时间
TIME_OUT = 30

# 项目数据存放路径，默认在当前新建项目下
DATA_PATH = './'

# 项目数据目录名称，默认data，系统会自动查找data目录下的数据到Case中
DATA_DIR = 'data'

# define定义的dict数据，最终在加载时被转换为json数据，当然也可以不进行转换，只要define参数中设置convert=None即可
DEFINE_CONVERT = 'json'
```

##搭建教程
###1.创建项目
在Mocker安装完毕后，在任意目录下执行`Mocker create exampleProject`命令
系统会根据模板自动构建新项目，如果当前目录下有同名文件夹，系统会提示目录已经存在，不予以创建
**创建目录结构**
```
    ---- exampleProject
        ---- data
             ---- exampleData.py
        ---- cases.py
        ---- request.py
        ---- settings.py
```

###2.准备数据
在新建的exampleProject/data目录下，模板定义数据例子，格式如下:
```python
from mocker.case import define
define('movies', {
    'name': 'Mocker',
    'desc': 'define example' 
})
```
**define(dataName, data, convert=dumpJson)**
1. `dataName`: 数据名称，在case中可以通过self.data直接引用
2. `data`：具体数据，可以时任意数据类型如dict，string，number等类型
3. `convert`: 可选转换器，对data数据进行加工，默认是进行json转换，可以自定义任意函数`convert=lambda x: return x`

###3.编写Case
exampleProject/cases.py文件，文件名称不局限于此，后期可以改为任意名称，但在执行用例时需明确名称`Mocker run exampleProject/newCases.py`
```python
from mocker.case import Case, report
from mocker.expect import Expect

from .request import TestExampleApi

class TestExampleCase(Case):
    data = 'examples'
    
    def init(self):
        self.exampleApi = TestExampleApi()

    @report(u'Test example')
    def testExample(self):
        # fetch data
        self.exampleApi.getExample()
        
        # validate response
        Expect(self.exampleApi.exampleResponse).code.eq(200)

    def run(self):
        self.testExample()

```
在cases.py文件中可以创建多个Case类，在执行`Mocker run exampleProject`时Cases.py中的所有继承于Case的类都会被执行
在定义Case类时需要注意几点：
1. 一定要继承Case父类
2. 类中有两个内置函数`init`,`run`，一个是类初始化时执行，一个是在最终执行时使用。其中`run`函数不能缺失
3. 类中`data='examples'`，字段是可选，值对应是当前项目`exampleProject/data/examples.py`文件，在类初始化时加载数据，`self.data`来引用数据
4. @report用于输出当前执行函数文案，可选（python2中针对report参数值需要加`u`前缀，python3中不需要）
