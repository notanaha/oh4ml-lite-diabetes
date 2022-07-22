# oh4ml-lite-diabetes

# setup

## conda environment for 200_prepareData.ipynb

```bash
conda env create -f environment.yml
conda activate env-oh4ml-lite-diabetes
conda install notebook ipykernel
ipython kernel install --user --name=env-oh4ml-lite-diabetes
```

## az login for az ml commands

```bash
az login --use-device-code
```

# run
Run in the following order
<br>
Confirm input/output configuration in a yml file before creating a job 
<br>

|  task    |  command  |
| ---- | ---- |
| Compute| az ml compute create -f 201_createAmlCompute.yml |
|  Environment  |  az ml environment create --file 202_createEnvironment-diabetes.yml  |
|  Training  |  az ml job create -f 203_trainOnRemote-diabetes.yml  |
|  evaluate  |  az ml job create -f 204_evaluate.yml  |
|  Model register  |  az ml job create -f 205_registerModel-diabetes.yml  |
|  Pipeline  |  az ml job create -f 206_pipeline-diabetes.yml  |
|  Batch endpoint  |  az ml batch-endpoint create --name ep-batch-oh4ml-01 --file endpoints/ep-batch-oh4ml-01.yml  |
|  Batch deployment #1  |  az ml batch-deployment create --name batch-deployment-01 --endpoint-name ep-batch-oh4ml-01 --file endpoints/batch-deployment-01.yml  |
|  Batch deployment #2  |  az ml batch-deployment create --name batch-deployment-02 --endpoint-name ep-batch-oh4ml-01 --file endpoints/batch-deployment-02.yml  |
|  Batch invoke #1  |  az ml batch-endpoint invoke --name ep-batch-oh4ml-01 --deployment-name batch-deployment-01 --input azureml:diabetes_query_oh4ml:2 --job-name batch-oh4ml-01  |
|  Batch invoke #2  |  az ml batch-endpoint invoke --name ep-batch-oh4ml-01 --deployment-name batch-deployment-02 --input azureml:diabetes_query_oh4ml:2 --job-name batch-oh4ml-02  |
|  Online endpoint |  az ml online-endpoint create --name ep-online-oh4ml-01 -f endpoints/ep-online-oh4ml-01.yml | 
|  Online deployment |  az ml online-deployment create --name blue --endpoint ep-online-oh4ml-01 -f endpoints/blue-online-oh4ml-01.yml --all-traffic |
|  Online invoke |  az ml online-endpoint invoke --name ep-online-oh4ml-01 --request-file endpoints/sample-request-diabetes.json |



