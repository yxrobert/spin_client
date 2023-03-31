#!/bin/bash -e

export PATH=/opt/protokitgo:/root/bin/jq:$PATH

env_file=/mnt/slots/cc-slots-land/batch/.env
lock_file=/home/user00/cc/cc-slots-land/cc-dev/dev-develop.lock
conf_file=~/jenkins/server_config.yaml
jk_file=/var/lib/docker/volumes/jenkins-data/_data

check_last_cmd() {
    if [ $? -ne 0 ]; then
        echo "failed execute - "${1}
        exit 1
    fi
}

yaml() {
    python -c "import yaml;print(yaml.safe_load(open('$1'))$2)"
}

urldecode() {
	python -c "import urllib;print(urllib.unquote('$1').decode('utf8'))"
}

file_lock() {
  if [[ ! -f "${lock_file}" ]]; then
    echo 1 > ${lock_file}
    echo "脚本可执行"
  else
    echo "脚本运行中，请稍后执行！"
    exit 1
  fi
}

file_unlock() {
  if [[ -f "${lock_file}" ]]; then
    rm -rf ${lock_file}
    echo "释放脚本锁"
  else
    echo "释放脚本锁(锁文件不存在)"
  fi
}

mod_branch() {
        gno=$[${1}+2]
        bno=$[${1}+3]
        gconf=$[${1}+4]
        bconf=$[${1}+5]

	echo "\nbefore setting"
	sed -n "${1},${bconf}p" $conf_file
	sed -i "${gno}c \ game: ${2}" $conf_file
	sed -i "${bno}c \ bandit: ${3}" $conf_file

	sed -i "${gconf}c \ cc-conf: ${4}" $conf_file
	sed -i "${bconf}c \ bandit-conf: ${5}" $conf_file
}

check_container() {
    exist=`docker inspect --format '{{.State.Running}}' $1`
    if [[ $exist == `false` ]];then
        echo $1" not OK"
        curl 'https://oapi.dingtalk.com/robot/send?access_token=13aa551ba8a79265c4424316089cd31c4f479b0f685f3d5a503b0ab6a1a42ec7' -H 'Content-Type: application/json'  -d '{"msgtype": "link","link": {"messageUrl": "'"${BUILD_URL}"'/console","title": "Jenkins-Server['"${1}"']-Failed","text": "check log for more detail"}}'
        exit 1
    else
        echo $1" Check"
    fi
}

check_whole_server() {
	check_container $1-backend
	check_container $1-rpc
	check_container $1-redis
	check_container $1-mongo
	check_container $1-fluentd
}

set_env_args() {
    echo "" > ${env_file}
    arr=(`echo ${variable_args} | tr ',' ' '`)
    echo ${arr[@]}
    for el in ${arr[*]}
    do
        echo $el
        echo -e ${el}=True >> ${env_file}
    done
}

clear_env_args() {
    echo "" > ${env_file}
}

check_env_args() {
    if [ "$1" = 'pkreview' ]; then
        echo "pkreview force ignore disable_rtp_limit"
        variable_args=$(echo ${variable_args} | sed -e 's/disable_rtp_limit,//g' | sed -e 's/disable_rtp_limit//g')
    fi
}

clear_ignore() {
    rm -rf ./gen/csharp
    rm -rf ./gen/js
    rm -rf ./gen/lua
    rm -rf ./gen/rawdata/csv
    rm -rf ./gen/rawdata/client
}
