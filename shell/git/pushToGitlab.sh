#!/usr/bin/env bash

scriptPath=/root/review_sites/git
FILENAME=projects.txt
cat $FILENAME | while read PROJECT
do
    echo "----------------------------------push $PROJECT"
    # change origin to gitlab
    cd ${scriptPath}/$PROJECT.git
    git push --all;git push --tags
    cd ..
done


# other projects not in projects.txt
echo "----------------------------------push noVNC"
cd ${scriptPath}/noVNC.git;
git push --all;git push --tags

echo "----------------------------------push spice-html5"
cd ${scriptPath}/spice-html5.git;
git push --all;git push --tags

echo "----------------------------------push pbr"
cd ${scriptPath}/pbr.git;
git push --all;git push --tags

