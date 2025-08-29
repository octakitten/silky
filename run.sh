#!/bin/bash
#build.sh



today=$( date +%s )

num=1

filename=$today-log.txt
while [ -e "$filename" ]; do
	filename='%s-%01d-log.txt'"$today""$(( ++num ))"
done

printf 'Using "%s" for the filename\n' "$filename"

folder="logs/"

mkdir -p "$folder"

.venv/bin/python3 -m ./run.py > "$folder$filename"
