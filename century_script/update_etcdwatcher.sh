source /root/jenkins/jk_func.sh

cd /mnt/slots/cc-server/server/cmd/etcdwatcher
git checkout feature/etcd_filter
git pull
#go get -u gitlab.funplus.io/cheesecake/cc-conf@deploy-cc-conf
#go mod tidy
#python gen.py
go build
check_last_cmd "config version not match"
mv -f etcdwatcher ~/jenkins

cd ../etcdfilter
go build
check_last_cmd "build etcd filter failed"
mv -f etcdfilter ~/jenkins

git reset --hard
echo done
