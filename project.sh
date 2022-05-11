#!/usr/bin/env bash

if [ $1 == "clean" ]; then
    rm -rf build dist CygnusX1.egg-info
    echo "This project was cleaned!!!"
elif [ $1 == "build" ]; then
    bash project.sh clean
    python3 setup.py sdist bdist_wheel
    twine check dist/*
    echo "This project was built!!!"
elif [ $1 == "release" ]; then
    bash project.sh clean
    python3 setup.py sdist bdist_wheel
    twine check dist/*
    twine upload dist/*
    echo "This project was released!!!"
elif [ $1 == "bumpversion" ]; then
    bumpversion --current-version $2 $3 setup.py cygnusx1/__init__.py --allow-dirty
    echo "Updated version!!!"
else
    echo "Unknow argument!!!"
    echo $@
fi