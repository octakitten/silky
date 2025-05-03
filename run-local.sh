#!/bin/bash

today=$( date +%s )

num=1

filename=$today-local.txt

while [ -e $filename ]; do
	filename='%s-%01d-log.txt' "$today" "$((++num))"
done

printf "Logging to %s\n" "$filename"

logfolder="$HOME"/.silky/logs"
venvpath="$HOME/.silky/.venv/bin/python3"
scriptpath="$HOME/.silky/run.py"

mkdir -p "$folder"

$venvpath $scriptpath > "$logfolder/$filename" 2>&1
