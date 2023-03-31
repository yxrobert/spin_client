# .bashrc

# User specific aliases and functions

export PATH=/root/go/bin:$PATH
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

alias tojk="cd /var/lib/docker/volumes/jenkins-data/_data"
alias etcdcp="cd /home/user00/cc/cc-slots-land/batch && ./etcd.sh pkcp"
alias etcddev="cd /home/user00/cc/cc-slots-land/batch && ./etcd.sh pktest"
alias gosvr="/mnt/slots/cc-slots-land/cc-dev/update_server.sh"
alias goetcd="nohup /usr/local/bin/etcd --advertise-client-urls http://10.0.84.74:2379,http://10.0.84.74:4001 --listen-client-urls http://10.0.84.74:2379,http://10.0.84.74:4001 &"

alias goview="./upLoadServer.sh -s pkreview -c release/v0.2.0 -bs release/v0.2.0 -bc release/v0.2.0 -pro dev -p 4444 -t game"
alias gojy="cd /home/user00/cc/cc-slots-land/cc-dev && ./upLoadServer.sh -s pkjy -c deploy-cc-conf -bs develop -bc  deploy-bandit-conf -pro dev -p 5555 -t game"
alias logjy="docker logs -f pkjy-backend"
alias logdev="docker logs -f pktest-backend"
alias godev="cd /home/user00/cc/cc-slots-land/cc-dev && ./upLoadServer.sh -s pktest -c deploy-cc-conf -bs develop -bc  deploy-bandit-conf -pro dev -p 6666 -t game"
alias logcp="docker logs -f pkcp-backend"
alias logyq="docker logs -f pkyq-backend"
alias gocp="cd /home/user00/cc/cc-slots-land/cc-dev && ./upLoadServer.sh -s pkcp -c deploy-cc-conf -bs develop -bc  deploy-bandit-conf -pro dev -p 9999 -t game"
alias goqa="cd /home/user00/cc/cc-slots-land/cc-dev && ./upLoadServer.sh -s pkyq -c deploy-cc-conf  -bs develop -bc deploy-bandit-conf -pro dev -p 3333 -t game"
alias gozxj="cd /home/user00/cc/cc-slots-land/cc-dev && ./upLoadServer.sh -s pkzxj -c deploy-cc-conf -bs develop -bc  deploy-bandit-conf -pro dev -p 8888 -t game"

alias goqar="cd /home/user00/cc/cc-slots-land/cc-dev && ./upLoadServer.sh -s pkyq -c release/0.0.1 -bs release/0.0.1 -bc release/0.0.1 -pro dev -p 3333 -t game"
alias golock="rm -rf /home/user00/cc/cc-slots-land/cc-dev/dev-develop.lock"
alias tojk="cd /var/lib/docker/volumes/jenkins-data/_data"

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

check_container() {
    count=`docker ps -a --filter name=^/$1`
    if [[ $count == 0 ]];then
        echo $1" not OK"
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


function random_id() {
	netstat_info=$(netstat -tlnp | grep tcp | awk '{print $4}' | cut -d: -f2)
	port=6379
	for i in {${1}..${2}}
	do
		flag=$(echo $netstat_info | grep  $i)
		if [ -z "$flag" ];then
			let "port=i"
			break
		fi
	done
	echo "$port"
}

rad_test() {
	#random_id $1 $2
	aa=$(random_id ${1} ${2})
	echo ${aa}
}

function docker_port() {
    docker ps -a | grep ${1} | awk -F '->' '{print $1}' | awk -F ':' '{print $3}'
}

function docker_pid() {
	docker ps -q | xargs docker inspect -f '{{.State.Pid}} {{.Config.Hostname}} {{.Name}}' | grep ${1}
}

function gogdb() {
	nsenter -t ${1} -m -p gdb -p ${2}
}
alias setgit="git config --global user.name 'chenpeng' && git config --global user.email 'peng.chen@centurygame.com' "

alias resetgit="git config --global user.email '' && git config --global user.name ''"

function gojenkins() {
	docker container run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind
	docker container run --name jenkins-blueocean --rm --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8083:8080 --publish 50000:50000 jenkinsci/blueocean
}

function gojk2() {
	docker container run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind
	docker container run --name jenkins-jenkins --rm --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8083:8080 --publish 50000:50000 jenkins/jenkins
}

alias goetcd="nohup /usr/local/bin/etcd --advertise-client-urls http://10.0.84.16:2379,http://10.0.84.16:4001 --listen-client-urls http://10.0.84.16:2379,http://10.0.84.16:4001 &"
alias godozzle="docker run --name dozzle -d --volume=/var/run/docker.sock:/var/run/docker.sock -p 8899:8080 amir20/dozzle:latest"
alias cws="check_whole_server"
alias gologview='docker run -d --name "log-viewer" -v "/root/install/log-viewer-1.0.1":"/log-viewer" -v "/mnt/slots/cc-slots-land/batch/":"/root/" -p "8111":"8111" --entrypoint "/log-viewer/logviewer.sh" openjdk:11'
