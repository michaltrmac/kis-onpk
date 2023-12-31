## Install Docker + Minikube
- Docker: https://docs.docker.com/engine/install/ubuntu/
- Minikube: https://minikube.sigs.k8s.io/docs/start/

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

## Kubernetes Tools
- [minikube](https://minikube.sigs.k8s.io/docs/start/) - local Kubernetes cluster
- [kubectl](https://kubernetes.io/docs/reference/kubectl/) - command line tool for communicating with a Kubernetes cluster’s
- [k9s](https://k9scli.io/) - terminal based UI to interact with Kubernetes clusters
- [kubectx & kubens](https://github.com/ahmetb/kubectx) - tools for easy switching between contexts and namespaces
