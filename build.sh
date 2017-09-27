#!/bin/bash

# env
NULL_PATH="$PWD"
NULL_PYPKG="$NULL_PATH/null"
NULL_TESTS="$NULL_PATH/tests"

# exports
export NULL_PATH
export NULL_PYPKG
export NULL_TESTS

# functions
function _build_py_pkg() {
    sudo python3 setup.py install
}

function _test_py_pkg () {
    python3 setup.py test
}

function _run_tests_manual () {
    for dir in $NULL_TESTS; do
        chmod +x "$NULL_TESTS/$dir"
        echo "Runing file : $dir"
        $NULL_TESTS$dir
    done
}

cmd="$1"
opt="$2"

if [ "$cmd" = "--build" ]; then
    _build__py_pkg
elif [ "$cmd" = "--test"] && [ "$opt" = "--manual" ]
    _run_tests_manual
elif [ "$cmd" = "--test" ] && [ "$opt" = "--py" ]; then
    _test_py_pkg
fi
