#!/bin/bash
PROGRAM_PATH=$(dirname "$(realpath "$0")")
APP_NAME=nezha-agent
CONF=$PROGRAM_PATH/agent.conf

case "$1" in
start)
    ${PROGRAM_PATH}/${APP_NAME} --disable-auto-update --disable-command-execute --disable-force-update -p $(get_property 'key') $( [ "$(get_property 'tls')" = true] && echo "--tls" || echo "" ) -s "$(get_property 'server')" > ${PROGRAM_PATH}/${APP_NAME}.log 2>&1 &
    echo $! > $PROGRAM_PATH/$APP_NAME.pid
    ;;
stop)
    if [ -e ${PROGRAM_PATH}/${APP_NAME}.pid ];then
        kill $(cat ${PROGRAM_PATH}/${APP_NAME}.pid)
        rm $PROGRAM_PATH/$APP_NAME.pid
    fi
    ;;
status)
    if [ -e ${PROGRAM_PATH}/${APP_NAME}.pid ];then
        echo "${APP_NAME} is runing..."
    else
        echo "${APP_NAME} is not runing..."
    fi
    ;;
restart)
    $0 stop
    $0 start
    ;;
*)
  echo "Usage: $0 {start|stop|status|restart}"
esac
# 正常退出程序
exit 0

function get_property {
    local key=$1
    grep -w "$key" "$CONF" | cut -d'=' -f2-
}