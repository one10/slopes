#!/bin/bash

temp_dir=`mktemp -d`

mv .git .gitignore .idea db00.sqlite3 venv $temp_dir

find . -name .mypy_cache | xargs rm -rf

zip -r slopes"`date "+%F"`".zip .

mv $temp_dir/.git .
mv $temp_dir/.gitignore .
mv $temp_dir/.idea .
mv $temp_dir/db00.sqlite3 .
mv $temp_dir/venv .

rmdir $temp_dir

#i-rw-r--r--@  1 macuser  staff    6148 Nov  2 02:52 .DS_Store
#drwxr-xr-x  15 macuser  staff     480 Nov  3 23:04 .git
#-rw-r--r--   1 macuser  staff    1839 Nov  1 22:27 .gitignore
#drwxr-xr-x   8 macuser  staff     256 Nov  2 02:34 .idea
#drwxr-xr-x   5 macuser  staff     160 Nov  1 19:55 .mypy_cache
#-rw-r--r--@  1 macuser  staff     452 Nov  1 21:43 README.md
#-rw-r--r--   1 macuser  staff  143360 Nov  1 22:21 db00.sqlite3
#-rw-r--r--   1 macuser  staff  147456 Nov  2 01:49 db_local.sqlite3
#drwxr-xr-x   6 macuser  staff     192 Nov  1 19:35 venv
