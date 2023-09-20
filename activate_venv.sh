#!/bin/bash
echo ${PWD}
/bin/bash -c "source ${PWD}/venv/bin/activate; exec /bin/bash -i"
