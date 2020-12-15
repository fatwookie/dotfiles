# My repo of dotfiles

This is my collection of dotfiles to build a sane shell environment. 

## Prerequisites

Just run:

```
sudo apt update -y ; sudo apt install -y fish curl python3 python3-pip \
  git tig mc vim; pip3 install invoke

wget https://github.com/dandavison/delta/releases/download/0.4.4/git-delta_0.4.4_amd64.deb

sudo dpkg -i git-delta_0.4.4_amd64.deb

git clone https://github.com/fatwookie/dotfiles

```

To deploy, run `~/.local/bin/invoke dotfiles`

*Warning!* 

This overwrites all existing copies of the equivalent files in this repo. Use with care!
