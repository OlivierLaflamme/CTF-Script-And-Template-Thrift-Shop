#!/bin/bash
#./tftpbatch files.txt "10.0.0.5:69"
#credit: https://unix.stackexchange.com/questions/76400/download-directory-structure-from-a-tftp-server

server="tftp://$2"

while IFS= read -r path; do
    [[ "$path" =~ ^\ *$ ]] && continue
    dir="$(dirname "$path")"
    printf "GET %s => %s\n" "$path" "$dir"
    ! [ -d "$dir" ] && mkdir -p "$dir"
    curl -o "$path" "$server/$path"
done < "$1"
