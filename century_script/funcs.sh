#!/bin/bash -e

get_container_id() {
	echo $(docker ps -n 1 --filter "name=$1" --format '{{.ID}}')
}

container_stop() {
	if [[ $# -ne 1 ]]; then
		error "input container name"
	fi
	CONTAINER=$1
	LAST_CONTAINER_ID=$(get_container_id "${CONTAINER}")
	if [[ ! -z ${LAST_CONTAINER_ID} ]]; then
		blue "reclaim resources: ${CONTAINER} ${LAST_CONTAINER_ID}"
		docker container stop ${LAST_CONTAINER_ID}
	fi

	LAST_CONTAINER_ID=$(get_container_id "${CONTAINER}")
	if [[ ! -z ${LAST_CONTAINER_ID} ]]; then
		docker container rm ${LAST_CONTAINER_ID} 2>/dev/null
	fi
}
export -f container_stop

parse_http_port() {
	if [[ $# -ne 1 ]]; then
		error "input ini file path"
	fi
	iniFile=$1
	port=$(head -3 ${iniFile} | tail -1 | awk '{print $3}')
	echo $port
}

function rand_port() {
    netstat_info=$(netstat -tlnp | grep tcp | awk '{print $4}' | cut -d: -f2)
    port=6379
    #for i in {${1}..${2}}
    for((i=$1; i<=$2; i++))
    do
        flag=$(echo $netstat_info | grep  $i)
        if [ -z "$flag" ];then
            let "port=i"
            break
        fi
    done
    echo "$port"
}
