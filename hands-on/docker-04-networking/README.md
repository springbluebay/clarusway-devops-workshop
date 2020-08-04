# Hands-on Docker-04 : Docker Networking

Purpose of the this hands-on training is to give the student understanding to networking in Docker.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- list available networks in Docker.

- create a network in Docker.

- inspect properties of a network in Docker.

- connect a container to a network.

- explain default network bridge configuration.

- configure user-defined network bridge.

- ping containers within same network.

- can bind containers to specific ports.

- delete Docker networks.

## Outline

- Part 1 - Launch a Docker Machine Instance and Connect with SSH

- Part 2 - Default Network Bridge in Docker

- Part 3 - User-defined Network Bridge in Docker

- Part 4 - Container Networking

## Part 1 - Launch a Docker Machine Instance and Connect with SSH

- Launch a Docker machine on Amazon Linux 2 AMI with security group allowing SSH connections using the [Cloudformation Template for Docker Machine Installation](../docker-01-installing-on-ec2-linux2/docker-installation-template.yml).

- Connect to your instance with SSH.

## Part 2 - Default Network Bridge in Docker

- Check if the docker service is up and running.

- List all networks available in Docker, and explain types of networks.

- Run two `alpine` containers with interactive shell, in detached mode, name the container as `clarus1st` and `clarus2nd`, and add command to run alpine shell. Here, explain what the detached mode means.

- Show the list of running containers on Docker machine.

- Show the details of `bridge` network, and explain properties (subnet, ips).

- Connect to the `clarus1st` container.

- Ping google.com four times to check internet connection.

- Ping `clarus2nd `container by its IP four times to show the connection.

- Try to ping `clarus2nd `container by its name, should face with bad address. Explain why failed (due to default bridge configuration not works with container names)

- Disconnect from `clarus1st` without stopping it (CTRL + p + q).

- Stop and delete the containers

## Part 3 - User-defined Network Bridge in Docker

- Create a bridge network `clarusnet`.

- List all networks available in Docker, and show the user-defined `clarusnet`.

- Show the details of `clarusnet`, and show that there is no container yet.

- Run four `alpine` containers with interactive shell, in detached mode, name the containers as `clarus1st`, `clarus2nd`, `clarus3rd` and `clarus4th`, and add command to run alpine shell. Here, 1st and 2nd containers should be in `clarusnet`, 3rd container should be in default network bridge, 4th container should be in both `clarusnet` and default network bridge.

- List all running containers and show there up and running.

- Show the details of `clarusnet`, and explain newly added containers. (1st, 2nd, and 4th containers should be in the list)

- Show the details of  default network bridge, and explain newly added containers. (3rd and 4th containers should be in the list)

- Connect to the `clarus1st` container.

- Ping `clarus2nd` and `clarus4th` container by its name to show that in user-defined network, container names can be used in networking.

- Try to ping `clarus3rd` container by its name and IP, should face with bad address because 3rd container is in different network.

- Ping google.com to check internet connection.

- Exit the `clarus1st` container without stopping and return to ec2-user bash shell.

- Connect to the `clarus4th` container, since it is in both network should connect all containers.

- Ping `clarus2nd` and `clarus4th` container by its name, ping `clarus3rd` container with its IP. Explain why used IP, instead of name.

- Stop and remove all containers

- Delete `clarusnet` network

## Part 4 - Container Networking

- Run a `nginx` web server, name the container as `ng`, and bind the web server to host port 8080 command to run alpine shell. Explain `--rm` and `-p` flags and port binding.

- Add a security rule for protocol HTTP port 8080 and show Nginx Web Server is running on Docker Machine.

- Stop container `ng`, should be removed automatically due to `--rm` flag.
