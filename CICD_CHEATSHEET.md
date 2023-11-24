## Prepare env - Minikube
```
# start k8s cluster
minikube start --nodes 1 --memory 2G

# enable ingress
minikube addons enable ingress
```

## Tekton - installation
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
```

## Tekton - dashboard
```
# install
kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/release.yaml

# port forward
kubectl --namespace tekton-pipelines port-forward svc/tekton-dashboard 9097:9097

# add --address flag with instance-ip if you want to have dashboard publicly available
kubectl --namespace tekton-pipelines --address localhost,<instance-ip> port-forward svc/tekton-dashboard 9097:9097
```

## Tekton - hello world
```
kubectl apply -f ./cicd/hello-world/task.yml
kubectl apply -f ./cicd/hello-world/task-run.yml
kubectl get taskrun hello-task-run
kubectl logs --selector=tekton.dev/taskRun=hello-task-run
```

## Tekton install tasks from catalog
```
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/git-clone/0.6/git-clone.yaml
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/buildah/0.6/buildah.yaml
```

## Tekton Pipeline - clone repo, build docker image, push to docker hub and deploy to k8s
### Prepare secrets

#### docker credentials
```
# docker login to hub.docker.com
docker login

# create base64 string for k8s secret
cat ~/.docker/config.json | base64 -w0

# paste result of previous command to docker-credentials.yml
```

#### git ssh
```
# create ssh key - without pass phrase
# add ssh key to github repo

# create base64 string of ssh key
cat ~/.ssh/id_rsa_github_passwordless | base64 -w 0

# paste result of previous command to git-credentials.yml
```

```
kubectl apply -f ./cicd/python-demo-app/git-credentials.yml
kubectl apply -f ./cicd/python-demo-app/docker-credentials.yml
kubectl apply -f ./cicd/python-demo-app/rbac.yml
kubectl apply -f ./cicd/python-demo-app/pipeline.yml
kubectl create -f ./cicd/python-demo-app/pipeline-run.yml
```

## Tekton - github trigger
### install triggers & interceptors
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml
kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/interceptors.yaml
```

### test github trigger
```
kubectl apply -f ./cicd/python-demo-app/github/
kubectl port-forward service/el-github-listener 8080
./cicd/python-demo-app/github/curl.sh
```