parallel --pipepart --block 100M -a $1 grep -P -f regexp.txt  > extracted-lines.txt
