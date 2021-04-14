#!/bin/bash
declare -A TOKENS
TOKENS[tree]="0xf0fcd737fce18f95621cc7841ebe0ea6efccf77e"
TOKENS[seed]="0x40B34cC972908060D6d527276e17c105d224559d"
BSCSCAN="https://bscscan.com/token/"

getvalue () {
curl -s "${1}${2}" | grep -A 3 "d-block" | grep span | grep -Eo "[0-9]{1,4}\.[0-9]{1,4}" | head -n 1;
};

getall () {
for keys in "${!TOKENS[@]}";
do
value=$(getvalue ${BSCSCAN} ${TOKENS[$keys]})
echo "\$ $keys $value"
done
};

######if you dont need decorations change the next block with just the
###### word getall to get the plain output
while true
do
    printer=$(getall)
    clear
    echo "$printer" | figlet | lolcat
    sleep 10
done

