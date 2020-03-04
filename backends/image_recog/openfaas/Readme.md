## Deploy the solution with OpenFaas

### Usage

- Set up a local OpenFaas cluster, as given here using [docker swarm](https://github.com/openfaas/workshop/blob/master/lab1.md)
- Set up faas-cli

```bash
curl -sSL https://cli.openfaas.com | sudo -E sh
```



- Pull in the faas template for Pytorch to this directory

```bash
faas-cli template pull https://github.com/rahulunair/faas_templates.git
```

2. Deploy the solution based on the configuration file `stack.yml`

```bash
faas-cli up -f stack.yml --gateway http://127.0.0.1:8080
```

If the deployment is successful, you will see:

```
Deployed. 202 Accepted.
URL: http://127.0.0.1:8080/function/img-recog-faas
```

Now you can use the web frontend to post requests to the FaaS service
