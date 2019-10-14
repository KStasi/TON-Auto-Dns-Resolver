#!/bin/sh
DOCKER_ID=`docker run -it -d dns_resolver`
echo "DOCKER_ID = $DOCKER_ID"
echo "#!/bin/bash" > ./docker_ssh.sh
echo "docker exec -t -i $DOCKER_ID /bin/bash" >> ./docker_ssh.sh
chmod +x ./docker_ssh.sh

echo "#!/bin/bash" > ./docker_drop.sh
echo "read -p 'are you sure? (press any key to continue)'" >> ./docker_drop.sh
echo "docker stop $DOCKER_ID" >> ./docker_drop.sh
echo "docker rm   $DOCKER_ID" >> ./docker_drop.sh
chmod +x ./docker_drop.sh

echo "#!/bin/bash" > ./docker_restart.sh
echo "docker restart $DOCKER_ID" >> ./docker_restart.sh
chmod +x ./docker_restart.sh

echo "#!/bin/bash" > ./docker_logs.sh
echo "docker logs $DOCKER_ID" >> ./docker_logs.sh
chmod +x ./docker_logs.sh

