
1. Pull in the faas template for Pytorch

```bash
faas-cli template pull https://github.com/rahulunair/faas_templates.git
```

2. Deploy the solution based on the configuration file `stack.yml`

```bash
faas-cli up -f stack.yml --gateway http://127.0.0.1:8080
```
