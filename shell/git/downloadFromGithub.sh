#!/usr/bin/env bash
# git clone --mirror https://github.com/openstack/swift.git
# git remote remove origin
# git remote add origin git@git.elenet.me:openstack/devstack.git
# git push --all;git push --tags;
# git branch -a

FILENAME=projects.txt
cat $FILENAME | while read PROJECT
do
    echo "----------------------------------processing $PROJECT"
    # clone from github
    git clone --mirror https://github.com/openstack/$PROJECT.git
    # change origin to gitlab
    cd $PROJECT.git
    git remote remove origin
    git remote add origin git@git.elenet.me:openstack/$PROJECT.git
    # push to gitlab
    git push --all;git push --tags;
    cd ..
done






