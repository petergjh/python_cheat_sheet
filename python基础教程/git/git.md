Git is a version control system. 
![git](https://gitee.com/PeterGao/pythonic/raw/master/python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/git/git.png)

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

