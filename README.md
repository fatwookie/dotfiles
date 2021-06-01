# My repo of dotfiles

This is my collection of dotfiles to build a sane shell environment. 

## Prerequisites

Just run:

```
sudo apt update -y ; sudo apt install -y tmux fish curl python3 python3-pip \
  git tig mc vim; pip3 install invoke

git clone https://github.com/fatwookie/dotfiles && cd dotfiles
sudo dpkg -i git-delta_0.6.0_amd64.deb

```

If you need a different version of `delta`, just download and install:

```
wget https://github.com/dandavison/delta/releases/download/0.6.0/git-delta_0.6.0_amd64.deb
sudo dpkg -i git-delta_0.6.0_amd64.deb
```

To deploy, run `~/.local/bin/invoke dotfiles`

*Warning!* 

This overwrites all existing copies of the equivalent files in this repo. Use with care!
