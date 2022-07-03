# oh4ml-lite-diabetes
Run in the following order
<br></br>

|  task    |  command  |
| ---- | ---- |
|  Environment  |  az ml environment create --file 201_createEnvironment-diabetes.yml  |
|  Training  |  az ml job create -n 02_trainOnRemtoe_oh4ml-01 -f 202_trainOnRemote-diabetes.yml  |
|  Model register  |  az ml job create -n 203_registerModel_oh4ml-01 -f 203_registerModel-diabetes.yml  |
|  Batch endpoint  |  az ml batch-endpoint create --name ep-batch-oh4ml-01 --file endpoints/ep-batch-oh4ml-01.yml  |
|  Batch deployment #1  |  az ml batch-deployment create --name batch-deployment-01 --endpoint-name ep-batch-oh4ml-01 --file endpoints/batch-deployment-01.yml  |
|  Batch deployment #2  |  az ml batch-deployment create --name batch-deployment-02 --endpoint-name ep-batch-oh4ml-01 --file endpoints/batch-deployment-02.yml  |
|  Batch invoke #1  |  az ml batch-endpoint invoke --name ep-batch-oh4ml-01 --deployment-name batch-deployment-01 --input azureml:diabetes_query_oh4ml:2 --job-name batch-oh4ml-01  |
|  Batch invoke #2  |  az ml batch-endpoint invoke --name ep-batch-oh4ml-01 --deployment-name batch-deployment-02 --input azureml:diabetes_query_oh4ml:2 --job-name batch-oh4ml-02  |
|  Pipeline  |  az ml job create -n 04_pipeline_oh4ml-01  -f 204_pipeline-diabetes.yml  |


