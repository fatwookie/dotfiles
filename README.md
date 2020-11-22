# My repo of dotfiles

This is my collection of dotfiles to build a sane shell environment. 

## Prerequisites

Just run:

```
sudo apt update -y ; sudo apt install -y fish curl ; pip3 install invoke

wget https://github.com/dandavison/delta/releases/download/0.4.4/git-delta_0.4.4_amd64.deb

sudo dpkg -i git-delta_0.4.4_amd64.deb

```

To deploy, run `invoke dotfiles`

*Warning!* 

This overwrites all existing copies of the equivalent files in this repo. Use with care!
