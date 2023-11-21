## Minikube
minikube start --nodes 1 --memory 8G

minikube addons enable dashboard
minikube addons enable metrics-server
minikube addons enable ingress

## Tekton - installation
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml

## Tekton - dashboard
kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/release.yaml
kubectl --namespace tekton-pipelines port-forward svc/tekton-dashboard 9097:9097

## Tekton - hello world
kubectl apply -f task.yml
kubectl apply -f task-run.yml
kubectl get taskrun hello-task-run
kubectl logs --selector=tekton.dev/taskRun=hello-task-run

## Tekton install tasks
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/git-clone/0.6/git-clone.yaml
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/buildah/0.6/buildah.yaml

## Tekton triggers
kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml
kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/interceptors.yaml

kubectl apply -f ./cicd/python-demo-app/github/
kubectl port-forward service/el-github-listener 8080
./cicd/python-demo-app/github/curl.sh

## Tekton - helm
kubectl apply -f https://api.hub.tekton.dev/v1/resource/tekton/task/helm-upgrade-from-source/0.3/raw