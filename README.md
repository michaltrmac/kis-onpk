## Minikube
### Start one node cluster
```bash
minikube start
```

### Start two node cluster
```bash
minikube start --nodes 2
```

### Start two node cluster with 4 GB RAM per cluster
```bash
minikube start --nodes 2 --memory 4G -p multinode-demo
```

## Kubernetes

### Create deployment
#### via kubectl command
```bash
kubectl create deployment web --image=gcr.io/google-samples/hello-app:1.0
```
#### via kubernetes manifest
```bash
kubectl apply -f ./k8s/web/deployment.yml
```

### Create service
#### via kubectl command
```bash
kubectl expose deployment web --type=NodePort --port=8080
```
#### via kubernetes manifest
```bash
kubectl apply -f ./k8s/web/service.yml
```

### Expose service from minikube
```bash
minikube service web
```