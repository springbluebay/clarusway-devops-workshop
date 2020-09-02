# Hands-on Docker-09 : Docker Swarm Networking, Managing Services, Secrets and Stacks

Purpose of the this hands-on training is to give students the understanding to the Docker Swarm basic operations.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- Explain the what Docker Swarm cluster is.

- Set up a Docker Swarm cluster.

- Deploy an application as service on Docker Swarm.

- Use `overlay` network in Docker Swarm.

- Update and revert a service in Docker Swarm.

- Create and manage sensitive data with Docker Secrets.

- Create and manage Docker Stacks.

## Outline

- Part 1 - Launch Docker Machine Instances and Connect with SSH

- Part 2 - Set up a Swarm Cluster with Manager and Worker Nodes

- Part 3 - Using Overlay Network in Docker Swarm

- Part 4 - Updating and Rolling Back in Docker Swarm

- Part 5 - Managing Sensitive Data with Docker Secrets

- Part 6 - Managing Docker Stack
  
## Part 1 - Launch Docker Machine Instances and Connect with SSH

- Launch `five` Compose enabled Docker machines on Amazon Linux 2 with security group allowing SSH connections using the of [Clarusway Docker Swarm Cloudformation Template](./clarusway-docker-swarm-cfn-template.yml).

- Connect to your instances with SSH.

```bash
```

## Part 2 - Set up a Swarm Cluster with Manager and Worker Nodes

- Prerequisites (Those prerequisites are satisfied within cloudformation template in Part 1)

  - Five EC2 instances on Amazon Linux 2 with `Docker` and `Docker Compose` installed.

  - Set these ingress rules on your EC2 security groups:

    - HTTP port 80 from 0.0.0.0\0

    - TCP port 2377 from 0.0.0.0\0

    - TCP port 8080 from 0.0.0.0\0

    - SSH port 22 from 0.0.0.0\0 (for increased security replace this with your own IP)

- Initialize `docker swarm` with Private IP and assign your first docker machine as manager:

```bash
```

- Check if the `docker swarm` is active or not.

```bash
```

- Get the manager token with `docker swarm join-token manager` command.

```bash
```

- Add second and third Docker Machine instances as manager nodes, by connecting with SSH and running the given command above.

```bash
```

- Add fourth and fifth Docker Machine instances as worker nodes.

```bash
```

- List the connected nodes in `Swarm`.

```bash
```

## Part 3 - Using Overlay Network in Docker Swarm

- List Docker networks and explain overlay network (ingress)

```bash
```

- Create a user defined overlay network.

```bash
```

- Explain user-defined overlay network (clarus-net)

```bash
```

- Create a new service with 3 replicas.

```bash
```

- List the tasks of `webserver` service, detect the nodes which is running the task and which is not.

```bash
```

- Check the URLs of nodes that is running the task with `http://<ec2-public-hostname-of-node>` in the browser and show that the app is accessible, and explain `Container Info` on the app page.

- Check the URLs of nodes that is not running the task with `http://<ec2-public-hostname-of-node>` in the browser and show that the app is not accessible.

- Add following rules to security group of the nodes to enable the ingress network in the swarm and explain `swarm routing mesh`.

  - For container network discovery -> Protocol: TCP,  Port: 7946, Source: security group itself

  - For container network discovery -> Protocol: UDP,  Port: 7946, Source: security group itself

  - For the container ingress network -> Protocol: UDP,  Port: 4789, Source: security group itself

- Check the URLs of nodes that is not running the task with `http://<ec2-public-hostname-of-node>` in the browser and show that the app is **now** accessible.

- Create a service for `clarusways/for-ping` and connect it clarus-net.

```bash
```

- List services

```bash
```

- List the tasks and go to terminal of ec2-instance which is running `for_ping` task.

```bash
```

- List the containers in ec2-instance which is running `for_ping` task.

```bash
```

- Connect the `for_ping` container.

```bash
```

- Ping the webserver service and explain DNS resolution. (When we ping the `Service Name`, it returns Virtual IP of `webserver`).

```bash
```

- Explain the `load balancing` with the curl command. (Pay attention to the host when input `curl http://webserver` )

```bash
```

- Remove the services.

```bash
```

## Part 4 - Updating and Rolling Back in Docker Swarm

- Create a new service of `clarusways/container-info:1.0` with 5 replicas.

```bash
```

- Explain `docker service update` command.

```bash
```

- Update `clarusways/container-info:1.0` image with `clarusways/container-info:2.0` image and explain the changes.

```bash
```

- Revert back to the earlier state of `webserver` service and monitor the changes.

```bash
```

- Remove the service.

```bash
```

## Part 5 - Managing Sensitive Data with Docker Secrets

- Explain [how to manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/).

- Create two files named `name.txt` and `password.txt`.

```bash
```

- Create docker secrets for both.

```bash
```

- List docker secrets.

```bash
```

- Create a new service with secrets.

```bash
```

- List the tasks and go to terminal of ec2-instance which is running `secretdemo` task.

```bash
```

- Connect the `secretdemo` container and show the secrets.

```bash
```

- To update the secrets; create another secret using `standard input` and remove the old one.(We can't update the secrets.)

```bash
```

- To check the updated secret, list the tasks and go to terminal of ec2-instance which is running `secretdemo` task.

```bash
```

- Connect the `secretdemo` container and show the secrets.

```bash
```

## Part 6 - Managing Docker Stack

- Explain `Docker Stack`.

- Create a folder for the project and change into your project directory
  
```bash
```

- Create a file called `wp_password.txt` containing a password in your project folder.

```bash
```

- Create a file called `docker-compose.yml` in your project folder with following setup and explain it.

```yaml
version: "3.7"

services:
    wpdatabase:
        image: mysql:latest
        environment:
            MYSQL_ROOT_PASSWORD: R1234r
            MYSQL_DATABASE: claruswaywp
            MYSQL_USER: clarusway
            MYSQL_PASSWORD_FILE: /run/secrets/wp_password
        secrets:
            - wp_password
        networks:
            - clarusnet
        volumes:
            - myvolume:/var/lib/mysql
    wpserver:
        image: wordpress:latest  
        depends_on:
            - wpdatabase
        deploy:
            replicas: 3
            update_config:
                parallelism: 2
                delay: 5s
                order: start-first
        environment:
            WORDPRESS_DB_USER: clarusway
            WORDPRESS_DB_PASSWORD_FILE: /run/secrets/wp_password
            WORDPRESS_DB_HOST: wpdatabase:3306
            WORDPRESS_DB_NAME: claruswaywp
        ports:
            - "80:80"
        secrets:
            - wp_password
        networks:
            - clarusnet
networks:
    clarusnet:
        driver: overlay

secrets:
    wp_password:
        file: wp_password.txt
volumes:
    myvolume:
```

- Deploy a new stack.

```bash
```

- List stacks.

```bash
```

- List the services in the stack.

```bash
```

- List the tasks in the stack

```bash
```

- Check if the `wordpress` is running by entering `http://<ec2-host-name>` in a browser.

- Remove stacks.

```bash
```
