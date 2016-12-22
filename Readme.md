My vim configuration

## Quick start

```shell
# setup vundle
cp vimrc ~/.vimrc
cp -r vim ~/.vim

# In Ubuntu
sudo apt-get install ctags

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
Launch vim and run :PluginInstall

# If needed
cd ~/.vim/bundle/YouCompleteMe
# For python 2.6+
sudo apt-get install python-dev
./install.py --all
# For python 3.3+
sudo apt-get install python3-dev
python3 install.py --all
```

## Work with screen

```shell
# Create a screen called dev
SCREEN_NAME='dev'
screen -dmS $SCREEN_NAME
```

