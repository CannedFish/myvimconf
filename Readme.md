My vim configuration

## Vim version

Based on YCM

Update to VIM8 on Ubuntu 1604
``` shell
sudo add-apt-repository ppa:jonathonf/vim
sudo apt-get update
sudo apt-get install vim
```

Update to VIM8 on CentOS
``` shell
curl -L https://copr.fedorainfracloud.org/coprs/mcepl/vim8/repo/epel-7/mcepl-vim8-epel-7.repo -o /etc/yum.repos.d/mcepl-vim8-epel-7.repo
yum update vim*
```

## Quick start

```shell
# setup vundle
cp vimrc ~/.vimrc
cp -r vim ~/.vim

# In Ubuntu
sudo apt-get install ctags
# In CentOS
sudo yum install ctags

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
Launch vim and run :PluginInstall
# vim-go will set local noexpendtab for go, makesure to comment it when you not need it.
Run :GoInstallBinaries for Golang

# Compile YCM if needed
cd ~/.vim/bundle/YouCompleteMe
# For python 2.6+
# In Ubuntu
sudo apt-get install python-dev
# In CentOS
sudo yum install python-devel
./install.py --all

# For python 3.3+
sudo apt-get install python3-dev
# In CentOS
sudo yum install python3-devel
python3 install.py --all
```

## Work with screen

```shell
# Create a screen called dev
SCREEN_NAME='dev'
screen -dmS $SCREEN_NAME
```

