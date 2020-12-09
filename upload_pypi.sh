#!/bin/bash
# ##########################################################################
# Author: txu
# Brief:  Upload xlogs to pypi
#
# Returns:
#   pass: 0
#   fail: not 0
# ##########################################################################

# pip install wheel
# pip install twine

rm -rf ./build ./xlogs.egg-info ./dist
python setup.py sdist bdist_wheel
twine upload  dist/*