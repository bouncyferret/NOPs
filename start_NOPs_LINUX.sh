#!/usr/bin/env bash
# add check to see if hfs20.0 exists.
cd /opt/hfs20.0/
source ./houdini_setup_bash
cd -

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

export NOPS="$SCRIPT_DIR/houdini"

export HOUDINI_PACKAGE_DIR="$NOPS/packages"
export HOUDINI_USER_PREF_DIR="$SCRIPT_DIR/temp_user_pref_dir/__HVER__"

# select random fonts - if enabled in nops_config.toml
# python $NOPS/random_font.py

houdini
