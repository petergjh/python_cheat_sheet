Git is a version control system. 
![git](https://gitee.com/PeterGao/pythonic/raw/master/python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/git/git.png)

### 创建版本库 
```
git init
```
git管理文件的目录称做版本库,又叫仓库,英文名repository
要新建一个版本库
第一步, 先新建一个空目录:
```
$ mkdir testgit
$ cd testgit
$ pwd
/d/git/testgit
```
pwd命令用来显示当前目录,下面我们把新建的git仓库放在这个位置/d/git/testgit

第二步, 用git init命令把这个目录变为git仓库:
```
$ git init
Initialized empty Git repository in D:/git/testgit/.git/
```
这样就新建了一个名为testgit的空git仓库(empty Git repository), 目录下自动生成了一个 隐藏目录 .git, 此目录用于跟踪管理版本变化.

### 添加文件 
```
git add
git commit
```

版本控制系统只能跟踪文本文件的改动，比如TXT文件，网页，程序代码等等，版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。而图片、视频这些二进制文件，虽然也能由版本控制系统管理，但没法跟踪文件的变化. 微软的Word格式是二进制,也无法用git管理.
建议使用标准的UTF-8编码进行文本编码.
Windows自带的记事本编辑任何文本文件。原因是Microsoft开发记事本的团队使用了一个非常弱智的行为来保存UTF-8编码的文件，他们自作聪明地在每个文件开头添加了0xefbbbf（十六进制）的字符，你会遇到很多不可思议的问题，比如，网页第一行可能会显示一个“?”，明明正确的程序一编译就报语法错误

下面新建并编辑一个文本文件readme.md到前面新建的testgit目录下
```
git is a version control software.
git is free.
```
md是markdown格式的文本文件,可理解成缩简版的html语言.

把一个文件放到Git仓库只需要两步。
第一步，用命令git add告诉Git，把文件添加到仓库：
```
$ git add readme.md
```
第二步，用命令git commit告诉Git，把文件提交到仓库：
```
$ git add readme.md

Administrator@CLZQXTBG9KYPI9V MINGW64 /d/git/testgit (master)
$ git commit -m 'edit a readme file'
[master (root-commit) 79f4c3a] edit a readme file
 1 file changed, 2 insertions(+)
 create mode 100644 readme.md
```
git commit命令，-m后面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录。

嫌麻烦不想输入-m "xxx"行不行？确实有办法可以这么干，但是强烈不建议你这么干，因为输入说明对自己对别人阅读都很重要。实在不想输入说明的童鞋请自行Google，我不告诉你这个参数。

git commit命令执行成功后会告诉你，1 file changed：1个文件被改动（我们新添加的readme.txt文件）；2 insertions：插入了两行内容（readme.txt有两行内容）。

commit可以一次提交很多文件，所以你可以多次add不同的文件，比如：
```
$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files."
```

### 查看版本状态 
```
git status
git diff
git log
git reflog
```

### 版本回退
```
git reset
```

git clone git@gitee.com:petergao/demo.git

git clone https://gitee.com/petergao/demo.git

git init

git add demo.txt

git commit -m "wrote a demo file"

git status

git diff

git diff HEAD -- demo.txt

git log

git log --pretty=oneline

git log --graph --pretty=oneline --abbrev-commit

git reflog

git reset HEAD demo.txt

git reset --hard HEAD^

git checkout -- demo.txt

git rm

ssh-keygen -t rsa -C "306739889@qq.com"

git remote -v

git remote add origin git@gitee.com:petergao/pythonic

git remote add mirror git@github.com:petergjh/pythonic

git remote rm origin

git push origin master

git push origin dev

git push -u origin master

git push -u mirror master

git rebase

git pull

git branch --set-upstream-to=origin/dev dev

git pull -u origin master

git pull -u mirror mastedr

git branch

git branch dev

git checkout dev

git checkou master

git checkout -b dev

git checkou -v feature-vulcan

git merge dev

git merge --no-off -m "merge with no-off" dev


git branch -v dev

git branch -D demo.txt

git stash

git stash list

git stash apply stas@{0}

git stash pop

git tag

git tag v1.0

git tag v0.9 f52c633

git show v0.0

git tag -d v0.1

git push origin v1.0

git push origin --tags

git push origin :refs/tags/v0.9

git config --global color.ui true

