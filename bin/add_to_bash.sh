# add these lines into ${HOME}/.bashrc
# if the file does not exist, create it
# possibly edit ROOT2GSA if you have not stored the directory gsa_2022
# in you HOME-directory

export ROOT2GSA=${HOME}/gsa_2022
export OPERATINGSYSTEM=`uname -s`
export PATH="${PATH}:${ROOT2GSA}/bin"
alias pys=${ROOT2GSA}/bin/pysearch.py
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
