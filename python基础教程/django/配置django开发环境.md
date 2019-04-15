系统环境: win7*64  
开发语言: python3.7   
web框架: django2.2   
版本控制: git  
IDE: idea+python插件   

# 环境检查: 
打开一个windows命令窗口cmd
```
python --version
pip --version
git --version
```
![.](https://gitee.com/PeterGao/pythonic/raw/master/python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/django/%E9%85%8D%E7%BD%AEdjango%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83/%E7%8E%AF%E5%A2%83%E6%A3%80%E6%9F%A5.JPG)
# 建立虚拟环境
* python3自带了venv,使用这个模块来创建一个虚拟环境来独立运行一个python项目
python -m venv 

* 早期的python版本如果不能用venv模块,可以安装virtualenv包来建立虚拟环境

VirtualEnv用于在一台机器上创建多个独立的python运行环境，VirtualEnvWrapper为前者提供了一些便利的命令行上的封装。

Virtualenv是一个非常好的virtual python environment builder，他最大的好处是，可以让每一个python项目单独使用一个环境，而不会影响python系统环境，也不会影响其他项目的环境。

Virtualenv可用于创建独立的Python环境，在这些环境里面可以选择不同的Python版本或者不同的Packages，并且可以在没有root权限的情况下在环境里安装新套件，互相不会产生任何的影响。

为什么要用virtualenv
- 隔离项目之间的第三方包依赖，如A项目依赖django1.2.5，B项目依赖django1.3。

- 为部署应用提供方便，把开发环境的虚拟环境打包到生产环境即可,不需要在服务器上再折腾一翻。在服务器上都不用安装virtualenv，直接将virtualenv创建的目录拷贝到服务器，修改路径，进行虚拟环境迁移就可以用了。

- 还可以用在没有root权限的python环境配置上，如果没有root权限，可以先自己搞一个virtualenv，再在virtualenv中使用pip安装。（系统中没有pip，并且也没有root权限使用sudo apt-get安装）

安装的库的位置
env/Lib/site-packages/目录里，而不是在系统的python的Lib/site-packages目录里，这样你就知道为什么虚拟环境是分开的了吧。

Note:virtualenv 创建的虚拟环境与主机的 Python 环境完全无关，你主机配置的库不能在 virtualenv 中直接使用。你需要在虚拟环境中利用 pip install 再次安装配置后才能使用。

