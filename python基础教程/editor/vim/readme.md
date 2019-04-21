### 让Vim不自动生成这些备份文件 

默认情况下使用Vim编程，在修改文件后系统会自动生成一个带*~*的备份文件，是以*~*结尾的 比如 new.txt~

让Vim不自动生成这些备份文件: 
1. 找到你的Vim安装目录一般为 /usr/share/vim/vim72，有 .vimrc.vim 文件打开修改; 如果是在Windows下默认路径安装的，应该是在C:/Program Files/Vim/ 找到这个文件：vimrc_example.vim 我的这个文件是在vim70文件夹下，具体还要看你安装的是什么版本的。 
2. 找到后打开，找到这一句：if has("vms") 
把这个判断里的if部分保留，else部分注释掉。 
（Vim的注释符是"） 
即修改后应该是这样的： 
if has("vms") 
set nobackup " do not keep a backup file, use versions instead 
" else 
" set backup " keep a backup file 
endif(别忘了，这个得保留着)

3. 如果没有 .vimrc.vim 文件，拷贝 vimrc_example.vim 文件到同一目录下，并重命名为.vimrc.vim， 然后再按照第二步修改；
cp vimrc_example.vim .vimrc.vim

4. 保存 退出。


