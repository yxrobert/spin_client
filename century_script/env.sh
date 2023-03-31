#!/bin/bash -e

export BLACK='\033[0;30m'
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export ORANGE='\033[0;33m'
export YELLOW='\033[1;33m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export NC='\033[0m'

blue() {
  echo -e "${CYAN}$*${NC}"
}
export -f blue
green() {
  echo -e "${GREEN}$*${NC}"
}
export -f green
red() {
  echo -e "${RED}$*${NC}"
}
export -f red
error() {
  red "$*"
  exit 1
}
export -f error

CMD=$(readlink -f "$0")
DIR=$(dirname -z "${CMD}")
while [[ "${DIR:(-14)}" != "/cc-slots-land" ]]; do
  DIR=$(dirname -z "${DIR}")
  if [[ "${DIR}" == "/" ]]; then
    error "exception"
  fi
done

export PROJECT_DIR="${DIR}"
ROOT_DIR=$(dirname -z "${PROJECT_DIR}")

export STAGE_DIR="${PROJECT_DIR}/stage"
if [[ ! -d ${STAGE_DIR} ]]; then
  mkdir "${STAGE_DIR}"
fi

export SRC_DIR="${ROOT_DIR}/cc-server"
export CODE_DIR="${SRC_DIR}"
export CONF_DIR="${ROOT_DIR}/cc-conf"
export BANDIT_CODE_DIR="${ROOT_DIR}/bandit-server"
export BANDIT_CONF_DIR="${ROOT_DIR}/bandit-conf"

export BUILD_DIR="/slots"
export BUILD_CONF_DIR="/cc-conf"

export GO_DIR="${PROJECT_DIR}/go"
export NODE_DIR="${SRC_DIR}/client/node_modules"

export BACKEND_COMPILE_IMAGE="slots/backend-builder:latest"
export BACKEND_RUN_IMAGE="golang:1.17-alpine"
export FRONTEND_RUN_IMAGE="slots/frontend:latest"
export REDIS_CLUSTER_IMAGE="grokzen/redis-cluster:latest"
export REDIS_IMAGE="redis:5.0.9"
export FLUENTD_IMAGE="fluentd:v1.9.1-1.0"
export MONGO_IMAGE="mongo:4.2.5"

export BACKEND_BUILD_CONTAINER="backend-builder"
export BACKEND_RUN_CONTAINER="backend"
export FRONTEND_RUN_CONTAINER="frontend"

export NETWORK="slots"
export MONGO_USER="root"
export MONGO_PASS="passwd"

if false; then
  for var in $(env | grep DIR | grep -v -e ZSH -e TMPDIR); do
    blue "$var"
  done
fi
