## Description
Encrypted secrets stored on the K8S cluster. 

* See: https://github.com/bitnami-labs/sealed-secrets#homebrew for CLI installation instructions.

* See: https://github.com/bitnami-labs/sealed-secrets/blob/main/docs/bring-your-own-certificates.md#try-your-own-certificates for how to seal your own secrets.

**NOTE:** You must have the public key info which was bootstrapped to the cluster.


Example to seal a secret:
```
export PUBLICKEY="/path/to/cert.crt"
kubeseal --cert "${PUBLICKEY}" --scope cluster-wide < mysecret.yaml -o yaml >> my_sealed_secret.yaml
```
The `mysecret.yaml` must contain a valid secret. Ex:

```
apiVersion: v1
kind: Secret
metadata:
  name: admin-user
  namespace: grafana
type: Opaque
stringData:
  username: XXXX
  password: XXXX
```