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
rpm -Uvh http://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el7.noarch.rpm
rpm --import http://mirror.ghettoforge.org/distributions/gf/RPM-GPG-KEY-gf.el7
yum -y remove vim-minimal vim-common vim-enhanced sudo
# run as root
yum -y --enablerepo=gf-plus install vim-enhanced sudo
```

## Quick start

```shell
# setup vundle
cp vimrc ~/.vimrc
cp -r vim ~/.vim

# In Ubuntu
sudo apt-get install ctags cmake
# In CentOS
sudo yum install ctags cmake

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
Launch vim and run :PluginInstall
# vim-go will set local noexpendtab for go, makesure to comment it when you not need it.
Run :GoInstallBinaries for Golang

# Compile YCM if needed
cd ~/.vim/bundle/YouCompleteMe

# For python 2
# In Ubuntu
sudo apt-get install python-dev
# In CentOS
sudo yum install python-devel

# If use system clang
# In Ubuntu
sudo apt-get install libclang-x.0-dev
# Install golang first
./install.py --clang-completer --system-libclang --go-completer

# Else, just
./install.py --all

# For python 3
sudo apt-get install python3-dev
# In CentOS
sudo yum install python3-devel
python3 install.py --clang-completer --system-libclang --go-completer
```

## Work with screen

```shell
# Create a screen called dev
SCREEN_NAME='dev'
screen -dmS $SCREEN_NAME
```

