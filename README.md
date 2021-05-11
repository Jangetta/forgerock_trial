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
Instructions for a Vanilla install of Minikube
1. To expose the application as an load balance service, we have to give our pod a namespace
```kubernetes
kubectl create namespace forgerock
```

2. To build the configmap for this enviroment, run the command below, pointing to the file, stock.txt. This will create the configmap called stock.yaml in yaml format, the file will not appear in your directory but is stored in kubernetes
```
kubectl create configmap stock.yaml --from-file stock.txt -o yaml
```

3. To build the secret config for this enviroment, run the command below, pointing to the file that contains the base64 version of the api_key.txt
```
echo -n "your_api_key_here" | base64 > secret.yaml
```

4. Apply both to your kubernetes instance
```
kubectl apply -f secret.yaml
kubectl apply -f stock.yaml
```

5. With this namespace created, we can apply the manifest file, forgerock_deploy.yaml, to the namespace
```Kube
kubectl apply -f forgerock_deploy.yaml -n forgerock
```

6. We can forward our port to see if our pod deployment was successful
```
kubectl port-forward deployment/forgerock-deploy -n forgerock 8081:8081
```

7. Navigate to localhost:8081 to see the flask application is successfully forwarding correctly

8. Run the forgerock_ingress.yaml with the command below to create a stable network for the pod, with the same namespace
```
kubectl apply -f forgerock_ingress.yaml -n forgerock
```

9. You can verify it is running if your output is similar to mine with the same command
```
MBP-041150:kubernetes julie.brady$ kubectl get svc -w
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   64m
^CMBP-041150:kubernetes julie.brady$ 
```
