minikube start

minikube start --nodes 3 --memory 4G -p multinode-demo

kubectl create deployment web --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment web --type=NodePort --port=8080
minikube service web