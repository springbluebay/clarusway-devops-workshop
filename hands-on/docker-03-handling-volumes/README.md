# Hands-on Docker-03 : Handling Docker Volumes

Purpose of the this hands-on training is to teach students how to handle volumes in Docker containers.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- explain what Alpine container is and why it is widely used.

- list available volumes in Docker.

- create a volume in Docker.

- inspect properties of a volume in Docker.

- locate the Docker volume mount point.

- attach a volume to a Docker container.

- attach same volume to different containers.

- delete Docker volumes.

## Outline

- Part 1 - Launch a Docker Machine Instance and Connect with SSH

- Part 2 - Data Persistence in Docker Containers

- Part 3 - Managing Docker Volumes

- Part 4 - Using Same Volume with Different Containers

## Part 1 - Launch a Docker Machine Instance and Connect with SSH

- Launch a Docker machine on Amazon Linux 2 AMI with security group allowing SSH connections using the [Cloudformation Template for Docker Machine Installation](../docker-01-installing-on-ec2-linux2/docker-installation-template.yml).

- Connect to your instance with SSH.

## Part 2 - Data Persistence in Docker Containers

- Check if the docker service is up and running.

- Run a `alpine` container with interactive shell open, and add command to run alpine shell. Here, explain explain what the alpine container is and why it is so popular. (Small size, Secure, Simple, Fast boot)

- Display the os release of the alpine container.

- Create a file named `short-life.txt` under `/home` folder

- Exit the container and return to ec2-user bash shell.

- Show the list of all containers available on Docker machine.

- Start the alpine container and connect to it.

- Show that the file `short-life.txt` is still there, and explain why it is there. (Container holds it data until removed).

- Remove the alpine container.

- Show the list of all containers, and the alpine container is gone with its data.

## Part 3 - Managing Docker Volumes

- Explain why we need volumes in Docker.

- List the volumes available in Docker, since not added volume before list should be empty.

- Create a volume named `cw-vol`.

- List the volumes available in Docker, should see local volume `cw-vol` in the list.

- Show details and explain the volume `cw-vol`. Note the mount point: `/var/lib/docker/volumes/cw-vol/_data`.

- List all files/folders under the mount point of the volume `cw-vol`, should see nothing listed.

- Run a `alpine` container with interactive shell open, name the container as `clarus`, attach the volume `cw-vol` to `/cw` mount point in the container, and add command to run alpine shell. Here, explain `--volume` and `v` flags.

- List files/folder in `clarus` container, show mounting point `/cw`, and explain the mounted volume `cw-vol`.

- Create a file in `clarus` container under `/cw` folder.

- List the files in `/cw` folder, and show content of `i-will-persist.txt`.

- Exit the `clarus` container and return to ec2-user bash shell.

- Show the list of all containers available on Docker machine.

- Remove the `clarus` container.

- Show the list of all containers, and the `clarus` container is gone.

- List all files/folders under the volume `cw-vol`, show that the file `i-will-persist.txt` is there.

## Part 4 - Using Same Volume with Different Containers

- Run a `alpine` container with interactive shell open, name the container as `clarus2nd`, attach the volume `cw-vol` to `/cw2nd` mount point in the container, and add command to run alpine shell.

- List the files in `/cw2nd` folder, and show that we can reach the file `i-will-persist.txt`.

- Create an another file in `clarus2nd` container under `/cw2nd` folder.

- List the files in `/cw` folder, and show content of `loadmore.txt`.

- Exit the `clarus2nd` container and return to ec2-user bash shell.

- Run a `ubuntu` container with interactive shell open, name the container as `clarus3rd`, attach the volume `cw-vol` to `/cw3rd` mount point in the container, and add command to run bash shell.

- List the files in `/cw3rd` folder, and show that we can reach the all files created earlier.

- Create an another file in `clarus3rd` container under `/cw3rd` folder.

- Exit the `clarus3rd` container and return to ec2-user bash shell.

- Run an another `ubuntu` container with interactive shell open, name the container as `clarus4th`, attach the volume `cw-vol` as read-only to `/cw4th` mount point in the container, and add command to run bash shell.

- List the files in `/cw4th` folder, and show that we can reach the all files created earlier.

- Try to create an another file under `/cw4th` folder. Should see error `read-only file system`

- Exit the `clarus4th` container and return to ec2-user bash shell.

- List all containers.

- Delete `clarus2nd`, `clarus3rd` and `clarus4th` containers.

- Delete `cw-vol` volume.
