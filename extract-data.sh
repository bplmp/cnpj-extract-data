7z x archive.zip || parallel --pipepart --block 100M -a 'F.K032001K.D81106D' grep -P -f regexp.txt  > extracted-lines.txt
