# Forgerock SRE Coding Test

## Docker Instructions
To download this specific docker image, use this command below: 
```docker
docker pull jangetta/forgerock_stock:0.1
```

To run this docker image, please run: 
```bash
Docker run - TID - P 5000:80 $image_ID
```

$Image_Id can be found by running:
```docker images```

output example:
```bash
MBP-041150:python julie.brady$ docker images
REPOSITORY                                                         TAG            IMAGE ID       CREATED          SIZE
jangetta/forgerock_stock                                           0.1            8c72c7ac8104   13 minutes ago   1.07GB
redis                                                              latest         987b78fc9e38   11 months ago    104MB
mongo                                                              latest         3f3daf863757   12 months ago    388MB
MBP-041150:python julie.brady$ 
```

My image_ID for this specific docker image is 8c72c7ac8104

My Dockerhub Profile is located [here](https://hub.docker.com/u/jangetta). 

## Kubernetes

