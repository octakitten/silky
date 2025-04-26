#!/bin/bash
build.sh



source ./.venv/bin/activate
#today=$( date +%Y%m&d )
printf -v today '%(%Y%m%d)T' -1

num=1

filename=$today-log.txt
while [ -e "$filename" ]; do
	printf -v filename '%s-%01d-log.txt' "$today" "$(( ++num ))"
done

printf 'Using "%s" for the filename\n' "$filename"

python3 ./run.py > "$filename"
