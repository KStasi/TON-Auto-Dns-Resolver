#!/bin/sh
while :
do
  echo "restart"
  screen -S iced -p 0 -X stuff "last
"
  screen -S iced -p 0 -X stuff "getaccount -1:fcb91a3a3816d0f7b8c2c76108b8a9bc5a6b7a55bd79f8ab101c52db29232260
"
  screen -S iced -p 0 -X hardcopy "hardscreen"
  python tuck_tuck.py
  sleep 1
done