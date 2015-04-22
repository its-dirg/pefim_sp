#!/bin/bash

make_metadata.py sp_conf > idp.xml
../src/pefim_sp/sp.py sp_conf service_conf