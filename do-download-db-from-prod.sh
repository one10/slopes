#!/bin/bash

scp -i ~/.ssh/oregon-2022-00.pem ec2-user@100.20.90.102:/var/app/current/db.sqlite3 .
