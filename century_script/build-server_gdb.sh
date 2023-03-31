#!/bin/bash -e

DIR=$(readlink -f "$0") && DIR=$(dirname "$DIR")
CONF_VERSION=$(grep cc-conf server/go.mod | cut -d " " -f 2)

cd "$DIR"
GIT_VERSION=$(./git-hash.sh)

. ./common.sh

green building '"'"${BIN}"'"'

DATE=$(TZ='Asia/Shanghai' date '+%Y-%m-%dT%H:%M:%S%z')
GO_VERSION=$(go version | awk '{print $3 " " $4}')

LDFLAGS="-X 'plutus/core.BuildGoVersion=${GO_VERSION}'"
LDFLAGS+=" -X 'plutus/core.BuildTime=${DATE}'"
LDFLAGS+=" -X 'plutus/core.BuildType=${TYPE}'"
LDFLAGS+=" -X 'plutus/core.BuildHost=${HOSTNAME}'"
LDFLAGS+=" -X 'plutus/core.BuildGit=${GIT_VERSION}'"
LDFLAGS+=" -X 'plutus/core.BuildConf=${CONF_VERSION}'"

cd ../cmd/main

TARGET="${PWD}/plutus-server-next"

echo -e "${ORANGE}LDFLAGS${NC} = ${CYAN}${LDFLAGS}${NC}"
echo -e "${ORANGE}TARGET${NC} = ${CYAN}${TARGET}${NC}"

go build -race -tags timetzdata -gcflags \"-N -l\" -ldflags "${LDFLAGS}" -o "${TARGET}" main.go \
  2> >(while read -r line; do red "${line}" >&2; done)
