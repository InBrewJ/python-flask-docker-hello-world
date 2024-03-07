# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t simple-flask-app:langford .
```

Run the Docker container using the command shown below.

```bash
$ docker run --rm -d -p 6666:5000 --name langford_willow simple-flask-app:langford
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:6666`
