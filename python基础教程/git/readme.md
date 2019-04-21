Git is a version control system. 

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
### 工作区（Workspace Directory）, 版本库（Repository）, 暂存区(Index或stage), 分支(branch)

![git](https://gitee.com/PeterGao/pythonic/raw/master/python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/git/git.png)

工作目录即工作区,比如前面新建的目录 testgit
工作区有一个隐藏目录 .git，这个不算工作区，而是Git的版本库
版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD
我们把文件往Git版本库里添加的时候，是分两步执行的：
第一步是用git add把文件添加进去，实际上就是把文件修改添加到暂存区；
第二步是用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支。
因为我们创建Git版本库时，Git自动为我们创建了唯一一个master分支，所以，现在，git commit就是往master分支上提交更改。
你可以简单理解为，需要提交的文件修改通通放到暂存区，然后，一次性提交暂存区的所有修改。
提交后，如果你又没有对工作区做任何修改，那么工作区就是“干净”的：
下面对readme.md做如下修改,
```
git is a version control software.
git is free.
git is powerful.
```
修改后再看下git的状态,
```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")
```
提示有过改动modified, 并且尚未添加到暂存区(not staged).

我们把修改后的文件用git add 来添加到暂存区(stage/index):
```
$ git add readme.md

$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   readme.md
```

git add命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行git commit就可以一次性把暂存区的所有修改提交到分支。
```
$ git commit -m 'stage/index work'
[master 3353a38] stage/index work
 1 file changed, 2 insertions(+)

$ git status
On branch master
nothing to commit, working tree clean
```
提交后，如果你又没有对工作区做任何修改，那么工作区就是“干净”的：working tree clean, 并且暂存区也是空的了nothing to commit.

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

### git cheat sheet
![git cheat sheet](https://gitee.com/PeterGao/pythonic/raw/master/python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/git/gitcheatsheet.JPG)

### 版本控制最佳实践
![a-succesfu-git-branching-model](https://gitee.com/PeterGao/pythonic/raw/master/python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/git/succesful-git-branching-model.JPG)

### ignore文件
不希望把本地不属于项目本身的一些附属文件同步到仓库上,就在库存里添加一个 .gitignore文件,在提交同步时就会忽略ignore文件里指定的类似文件.

文件名是 .gitignore
```
#git push ignore


#markDown
*.md.un~

#Windows
Thumbs.db
ehthumbs.db
Desktop.ini

#Python
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

#IntelliJ IDEA Files
*.iml
*.ipr
*.iws
*.idea
```
请参考同目录的一个范例ignore模版


