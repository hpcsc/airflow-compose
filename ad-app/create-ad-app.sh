#!/bin/bash

set -euo pipefail

APP_NAME=$1

SCRIPT_DIR=$(cd $(dirname $0); pwd)

# Microsoft Graph resource app id: 00000003-0000-0000-c000-000000000000
# profile scope id: 14dad69e-099b-42c9-810b-d002981feec1
APP_CREATION_OUTPUT=$(az ad app create \
    --display-name ${APP_NAME} \
    --credential-description default \
    --reply-urls http://localhost:8080/oauth-authorized/azure \
    --required-resource-accesses @${SCRIPT_DIR}/resource-accesses.json \
    --optional-claims @${SCRIPT_DIR}/optional-claims.json \
    -o json)

APP_ID=$(echo ${APP_CREATION_OUTPUT} | jq -r '.appId')

echo "=== Application with id ${APP_ID} created"

az ad app credential reset --credential-description default --id ${APP_ID} -o json
echo "=== Client secret for app ${APP_ID} reset"

# az ad app permission admin-consent --id ${APP_ID}
