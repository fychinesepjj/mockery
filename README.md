#Mockery使用说明
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
    * 其他

##项目说明
　　Mockery的名称源于Mock，英文原意是模仿者的意思，开发Mockery的主要目的是减轻测试者在黑盒测试某些不必要环节的工作量，提高黑盒测试整体运作效率。不同于以往的黑盒测试，Mockery对使用者有一定的编程要求，但又不至于像白盒测试那么高，介于二者之间。
  
　　Mockery最大的特点是灵活性高，最大不足是覆盖面较窄，主要用途是完成黑盒测试中对API结果的验证。
  
　　为了降低Mockery的使用门槛，加快项目的创建，Mockery引入了一些快捷指令如：`run`，`create`等，让使用者更容易掌握。


##项目结构
```
    ---- mockery
        ---- conf
             ---- global_settings.py
             ---- __init__.py 
             ---- project_template
        ---- bin
             ---- __init__.py 
             ---- mockery-manager.py  #部署后，命令脚本
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
  * cookiecutter>=1.4.0

  可使用`pip install -r requirements.txt`安装


###Mockery安装方法
  1. 下载安装最新版本[python](https://www.python.org/downloads/)
  2. `git clone xxx` or 直接下载源码gz文件
  3. 打开或解压源码文件夹
  4. 进入./dist目录
  5. 执行安装命令`pip install Mockery-xxx.zip` (此方法会检查第三方依赖，如不存在会自动下载安装)
  6. 打开命令控制台
     * window下执行win+R，输入cmd，进入命令提示符界面
     * linux 可直接打开命令提示符界面
     * 输入`python`命令，执行`import mockery;mockery.VERSION`查看安装是否成功

###其他
  * 需要升级mockery，可以下载最新版本，同样执行上述安装步骤即可
  * 需要卸载mockery，执行`pip uninstall mockery`进行卸载
  * 如果需要mockery依赖一同卸载，下载`pip install pip-autoremove`, 执行`pip-autoremove mockery`进行卸载
  * 后续mockery会提交pip库，方便下载


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
在Mockery安装完毕后，在任意目录下执行`mockery create exampleProject`命令（windows如有权限问题，可使用`mockery-manager.py create exampleProject`命令替代）

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
from mockery.case import define
define('movies', {
    'name': 'mockery',
    'desc': 'define example' 
})
```
**define(dataName, data, convert=dumpJson)**
  1. `dataName`: 数据名称，在case中可以通过self.data直接引用
  2. `data`：具体数据，可以时任意数据类型如dict，string，number等类型
  3. `convert`: 可选转换器，对data数据进行加工，默认是进行json转换，可以自定义任意函数`convert=lambda x: return x`

###3.编写Case
exampleProject/cases.py文件，默认命名cases.py，后期可选任意名称
但在执行用例时需明确名称`mockery run exampleProject/newCases.py`
```python
from mockery.case import Case, report
from mockery.expect import Expect

from .request import TestExampleApi

class TestExampleCase(Case):
    data = 'examples'
    
    def init(self):
        # 初始化请求
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
在cases.py文件中可以创建多个Case类，在执行`mockery run exampleProject`时Cases.py中的所有继承于Case的类都会被执行
在定义Case类时需要注意几点：
  1. 需要继承Case父类
  2. 类中有两个内置函数`init`,`run`，一个是类初始化时执行，一个是在最终执行时使用，其中`run`函数不能缺失
  3. 类变量`data='examples'`可选，值对应当前项目`exampleProject/data/examples.py`文件，在类初始化时加载数据，`self.data`引用数据
  4. @report用于输出当前执行函数文案，可选（python2中针对report参数值需要加`u`前缀，python3中不需要）
  5. Expect接受Api的response对象作为参数，也接受普通数据类型如`str`, `int`等，`Expect(200).eq(200)`
  6. Expect对象几个常用函数（A：输入数据，B：需要匹配数据）:
    * `eq` 比较数值类型，A == B
    * `toBe` 比较`object`，`str`，`int`类型， A == B
    * `lt`，`gt` 比较数值类型，A < B，A > B
    * `match`，比较 `dict`，`str`，`int`，其中dict类型支持部匹配，B如果是A的子集，同样也会返回`True`

###4.数据请求
####基本结构
exampleProject/request.py文件，默认命名request.py，后期可选任意名称
```python
from mockery.request import Request, Api, catch
# 创建请求
req = Request()

class TestExampleApi(Api):
    @req.get('http://localhost/example.json')
    @checkStatus(code=200)
    @catch
    def getExample(self, res):
        self.getResponse = res
    
    @req.post('http://localhost/example.json')
    @catch
    def postExample(self, res):
        self.postResponse = res
        
```
request模块主要在`Cases.py`中使用，在`init`函数中初始化
**Request(session=False)**
* `session`:可选参数，默认关闭，主要作用是保存请求状态，用于需要登陆的Api使用
Request对象提供两种请求：`get`, `post`
使用方法：
  1. `@req.get('http://localhost/example.json')`
  2. `@req.post('http://localhost/example.json')`

####函数钩子
  * `@catch`用于捕获`getExample`方法中抛出的异常，建议新建函数都加上。
  * `@checkStatus`强制约定Api返回的状态码必须为某个值`@checkStatus(code=200)`，否则给予错误提示

####发送数据
如果需要向Api发送数据，`getExample`默认接受几类参数：
`GET`方法：
  1. `getExample()` 直接发送请求，无附带参数
  2. `getExample(data={name:'abc', age:12})` == `getExample(param={name:'abc', age:12})` url附带数据

`POST`方法：
  1. `postExample(data={'name':'abc', 'age': 12})` form数据
  2. `postExample(json={'data': {'name':'abc', 'age': 12}})` json数据
  3. `postExample(files = {'file': open('touxiang.png', 'rb')})` 文件对象
  4. `postExample(cookies = {'cookies_are':'working'})` cookies
  5. `postExample(headers = {'content-type': 'application/json'})` headers

###5.执行用例
执行用例有两种方法：
  1. 在当前Project目录中执行 `mockery run cases.py`，针对某个Case文件执行
  2. 在Project上一层目录中执行 `mockery run projectName`，针对某一项目执行，系统自动查找项目下名为`cases.py`的文件执行

第一种方法灵活性高，但需要具体的Case文件名
第二种方法针对项目运行，简单易用，要求项目必须有名为`cases.py`的文件

##其他
  1. window下安装，执行`mockery`可能会出现各种错误，大部分情况下是因为权限问题，以管理员身份运行即可
  2. 由于时间关系，测试代码覆盖不够完整，因此可能会出现异常问题，请及时反馈给我，后期代码会逐步完善，敬请原谅！