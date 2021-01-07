#!/usr/bin/env bash

DIRECTORY=virtualenvs/.env
deactivate 2> /dev/null
if [ -d "${DIRECTORY}" ]; then
    source ${DIRECTORY}/bin/activate
else
    python3 -m venv ${DIRECTORY}
    source ${DIRECTORY}/bin/activate
fi

serve() {
    uvicorn app:app --host 0.0.0.0 --reload
}