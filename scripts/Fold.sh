#! /bin/bash
PREFIX="$1"
echo $PREFIX
for item in `ls "${PREFIX}"`;
    do
        dir="${PREFIX}/$item"
        # ls -l "$PREFIX/$item"
        if [ -d "$dir" ]; then
            for file in `ls "$dir"|grep .mkv`;
            do
                mv "$dir/$file" "$PREFIX"
                #echo "mv \"$dir/$file\" \"$dir\""
            done
            rm -R "$dir"
        fi
    done