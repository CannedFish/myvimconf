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
# 1. Download and update to latest python;
  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-dev

  mv /usr/bin/python /usr/bin/python2.7.5
  ln -s /usr/local/bin/python2.7 /usr/bin/python # 增加软链接

  wget  https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tar.xz
  tar xf Python-2.7.14.tar.xz
  cd Python-2.7.14

  ./configure --enable-optimizations --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
  make && sudo make altinstall

  # vi /usr/bin/yum
  # change #!/usr/bin/python to #!/usr/bin/python2.7
  # vi /usr/libexec/urlgrabber-ext-down
  # change #!/usr/bin/python to #!/usr/bin/python2.7

  wget https://bootstrap.pypa.io/get-pip.py
  python get-pip.py
  whereis pip #查找pip的位置
  mv /usr/bin/pip /usr/bin/pip.bak
  ln -s /usr/local/bin/pip2.7 /usr/bin/pip

# 2. Download and update to latest cmake;
yum autoremove cmake
wget https://cmake.org/files/v3.7/cmake-3.7.1.tar.gz
tar xzf cmake-3.7.1.tar.gz
cd cmake-3.7.1
./bootstrap
gmake -j$(nproc)
make install
cd ..
rm -fr cmake*)

# 3. Download and update to latest clang;
yum install yum-utils 
yum-builddep -y llvm clang
wget https://bootstrap.pypa.io/ez_setup.py -O - | python
easy_install pip
pip install distribute

wget http://llvm.org/releases/3.9.1/llvm-3.9.1.src.tar.xz
wget http://llvm.org/releases/3.9.1/cfe-3.9.1.src.tar.xz
wget http://llvm.org/releases/3.9.1/compiler-rt-3.9.1.src.tar.xz
wget http://llvm.org/releases/3.9.1/clang-tools-extra-3.9.1.src.tar.xz
tar xf llvm-3.9.1.src.tar.xz
mv llvm-3.9.1.src llvm
cd llvm/tools
tar xf ../../cfe-3.9.1.src.tar.xz
mv cfe-3.9.1.src clang
cd clang/tools
tar xf ../../../../clang-tools-extra-3.9.1.src.tar.xz
mv clang-tools-extra-3.9.1.src extra
cd ../../../projects
tar xf ../../compiler-rt-3.9.1.src.tar.xz
mv compiler-rt-3.9.1.src compiler-rt
cd ../..
mkdir llvm-build
cd llvm-build
cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/lib/llvm-3.9.1 -DLLVM_OPTIMIZED_TABLEGEN=1 ../llvm
make -j$(nproc)
make install

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
cp screenrc $HOME/.screenrc
# Create a screen called dev
SCREEN_NAME='dev'
screen -dmS $SCREEN_NAME
```

## Work with tmux

```shell
cp tmux.conf $HOME/.tmux.conf

tmux new -s $<session-name>
tmux att -t $<session-name>
```
