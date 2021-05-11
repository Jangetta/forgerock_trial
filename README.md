# forgerock_trial

To download docker image, use this command below: 
docker pull jangetta/forgerock_stock:0.1

To run docker image, please run: 
Docker run - TID - P 5000:80 $image_ID

$Image_Id can be found by running, docker images in the terminal, output example:

MBP-041150:python julie.brady$ docker images
REPOSITORY                                                         TAG            IMAGE ID       CREATED          SIZE
jangetta/forgerock_stock                                           0.1            8c72c7ac8104   13 minutes ago   1.07GB
redis                                                              latest         987b78fc9e38   11 months ago    104MB
mongo                                                              latest         3f3daf863757   12 months ago    388MB
MBP-041150:python julie.brady$ 

My image_ID for this specific dockerimage is 8c72c7ac8104

