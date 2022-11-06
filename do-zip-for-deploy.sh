#!/bin/bash

rm *zip
temp_dir=`mktemp -d`

mv .git .gitignore .idea venv $temp_dir

find . -name .mypy_cache | xargs rm -rf

zip -r slopes"`date "+%F"`".zip .

mv $temp_dir/.git .
mv $temp_dir/.gitignore .
mv $temp_dir/.idea .
mv $temp_dir/db00.sqlite3 .
mv $temp_dir/venv .

rmdir $temp_dir

