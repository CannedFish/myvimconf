My vim configuration

## Quick start

```shell
# setup vundle
cp vimrc ~/.vimrc
cp -r vim ~/.vim

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
Launch vim and run :PluginInstall
```

## work with screen

```shell
# Create a screen called dev
SCREEN_NAME='dev'
screen -d -m -S $SCREEN_NAME -t shell -s /bin/bash
```

