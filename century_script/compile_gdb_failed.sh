#!/bin/bash

source env.sh

debug_env

TARGET_NAME="game"
if [[ $# -eq 2 ]]; then
  TARGET_NAME="$2"
fi

CONF_PROD="_prod"
CONFIG_FILE="${APP}/config.ini"
CONFIG_FILE_PROD="${APP}/config${CONF_PROD}.ini"

DATE=$(TZ='Asia/Shanghai' date '+%Y-%m-%dT%H:%M:%S%z')
TARGET="/slots/server/cmd/main/plutus-server-next"

BUILD_TARGET_GAME="cd proto && make server -B && cd ../server/cmd/main && go build -gcflags \"-N -l\" -race -tags timetzdata -ldflags '-X main.buildTime=${DATE}' -o '${TARGET}' main.go && pwd && ls"
BUILD_TARGET_ALL=$(
  cat <<-BUILD_CMD
make proto -B &&
  server/output/build-server.sh docker &&
  server/output/build-svr.sh idService &&
  server/output/build-svr.sh lighthouse
BUILD_CMD
)

BUILD_TARGET=$BUILD_TARGET_GAME
if [[ "${TARGET_NAME}" == "all" ]]; then
  BUILD_TARGET="${BUILD_TARGET_ALL}"
fi

echo -e "${YELLOW}    BUILD TARGET:${NC} ${TARGET_NAME}"
echo -e "${YELLOW}   BUILD COMMAND:${NC} ${BUILD_TARGET}"
echo -e "${YELLOW}           IMAGE:${NC} ${BACKEND_COMPILE_IMAGE}"
echo -e "${YELLOW}       CONTAINER:${NC} ${BACKEND_BUILD_CONTAINER}"
echo -e "${YELLOW}          GO_DIR:${NC} ${GO_DIR}"
echo -e "${YELLOW}        CODE_DIR:${NC} ${CODE_DIR}"
echo -e "${YELLOW}        CONF_DIR:${NC} ${CONF_DIR}"
echo -e "${YELLOW}       BUILD_DIR:${NC} ${BUILD_DIR}"
echo -e "${YELLOW}  BUILD_CONF_DIR:${NC} ${BUILD_CONF_DIR}"
echo -e "${YELLOW}     CONFIG_FILE:${NC} ${CONFIG_FILE}"
echo -e "${YELLOW}CONFIG_FILE_PROD:${NC} ${CONFIG_FILE}"

MOUNT_CONF_LOADER="${CONF_DIR}"/gen/golang/conf:"${BUILD_DIR}"/server/pkg/gen/golang/conf
MOUNT_CONF_MODEL="${CONF_DIR}"/gen/golang/rawdata:"${BUILD_CONF_DIR}"/gen/golang/rawdata

if true; then
  green "MOUNT_CONF_LOADER => ${MOUNT_CONF_LOADER}"
  green " MOUNT_CONF_MODEL => ${MOUNT_CONF_MODEL}"
fi

container_stop "${BACKEND_BUILD_CONTAINER}"

cmd=$(
  cat <<-DOCKER_CMD
docker run -it \
  --name "${BACKEND_BUILD_CONTAINER}" \
  --hostname "${BACKEND_BUILD_CONTAINER}" \
  -v "${GO_DIR}":/go \
  -v "${CODE_DIR}":"${BUILD_DIR}" \
  -v "${CONF_DIR}":"${BUILD_CONF_DIR}" \
  -v "${MOUNT_CONF_LOADER}" \
  -v "${MOUNT_CONF_MODEL}"  \
  "${BACKEND_COMPILE_IMAGE}" \
  sh -c "${BUILD_TARGET}"
DOCKER_CMD
)

blue "$cmd"
eval "$cmd"

# shellcheck disable=SC2181
if [[ $? -ne 0 ]]; then
#  docker logs "${BACKEND_BUILD_CONTAINER}"
  error "build failed"
fi

green "reset app dir: ${APP_DIR}"
/bin/rm -rf "${APP_DIR}"
mkdir -p "${APP_DIR}"

green 'copy compiled binary to app dir...'
if [[ "${TARGET_NAME}" == "game" ]]; then
  red "docker container cp ${BACKEND_BUILD_CONTAINER}:${BUILD_DIR}/server/cmd/main/plutus-server-next ${APP_DIR}/plutus-server"
  docker container cp "${BACKEND_BUILD_CONTAINER}:${BUILD_DIR}/server/cmd/main/plutus-server-next" "${APP_DIR}/plutus-server"
fi
if [[ "${TARGET_NAME}" == "all" ]]; then
  docker container cp "${BACKEND_BUILD_CONTAINER}:${BUILD_DIR}/server/cmd/main/plutus-server-next" "${APP_DIR}/plutus-server"
  docker container cp "${BACKEND_BUILD_CONTAINER}:${BUILD_DIR}/server/cmd/idService/idService" "${APP_DIR}/idService"
  docker container cp "${BACKEND_BUILD_CONTAINER}:${BUILD_DIR}/server/cmd/lighthouse/lighthouse" "${APP_DIR}/lighthouse"
fi

green "copy server config: ${CONFIG_FILE} ${APP_DIR}/config.ini"
/bin/cp "${CONFIG_FILE}" "${APP_DIR}/config.ini"
/bin/cp "${CONFIG_FILE_PROD}" "${APP_DIR}/config${CONF_PROD}.ini"

if false; then
  if [[ ! -d "${APP_DIR}/subject" ]]; then
    mkdir "${APP_DIR}/subject"
  fi
  /bin/cp "${SUBJECT_DIR}/"*.* "${APP_DIR}/subject/"
fi

green "remove container: ${BACKEND_BUILD_CONTAINER}"
container_stop "${BACKEND_BUILD_CONTAINER}"
