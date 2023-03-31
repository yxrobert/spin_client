#!/bin/bash -e

. ./env.sh

STAGE_DIR=$(realpath $STAGE_DIR)
echo "STAGE_DIR: ${STAGE_DIR}"
if [[ -z ${STAGE_DIR} ]]; then
	echo 'STAGE_DIR error'
	exit 1
fi
if [[ ${#STAGE_DIR} -eq 1 && "${STAGE_DIR:0:1}" == "/" ]]; then
	echo 'STAGE_DIR critical'
	exit 1	
fi

/bin/rm -rf ${STAGE_DIR}/*
