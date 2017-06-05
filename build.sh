#!/bin/sh -xe

# This script starts docker and systemd (if el7)

# Version of CentOS/RHEL
el_version=$1

docker build --tag chef_docker_builder .

if test "${TRAVIS}" == "true"
then
	BUILD_NUMBER=${TRAVIS_BUILD_NUMBER}
else
	BUILD_NUMBER="localbuild"
fi

echo $BUILD_NUMBER
export BUILD_NUMBER

 # Run build in Container
docker run --env BUILD_NUMBER --volume `pwd`:/spec_src chef_docker_builder role_webserver.spec
#DOCKER_CONTAINER_ID=$(docker ps | grep chef_docker_builder | awk '{print $1}')
#docker logs $DOCKER_CONTAINER_ID
#docker exec -ti $DOCKER_CONTAINER_ID /bin/bash -xec "bash -xe /htcondor-ce/tests/test_inside_docker.sh ${OS_VERSION};
#docker ps -a
#docker stop $DOCKER_CONTAINER_ID
#docker rm -v $DOCKER_CONTAINER_ID
