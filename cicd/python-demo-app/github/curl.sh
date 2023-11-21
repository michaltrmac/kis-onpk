secret="1234567"
event="pull_request"
commit_sha=$(git rev-parse HEAD)
payload='{"action": "opened", "'${event}'":{"head":{"sha": "'${commit_sha}'"}},"repository":{"clone_url": "https://github.com/tektoncd/triggers.git"}}'
hmac=$(echo -n ${payload} | openssl sha1 -hmac ${secret} | sed -e 's/^.* //')

curl -v \
-H "X-GitHub-Event: ${event}" \
-H "X-Hub-Signature: sha1=${hmac}" \
-H "Content-Type: application/json" \
-d "${payload}" \
http://localhost:8080