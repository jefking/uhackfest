# Azure Batch
https://azure.microsoft.com/en-us/services/batch/

## Outcome
Batch environment capable of scaling up a handful of machines that leverages low priority VMs.

Blob->Event Grid->X->Job+Task->Batch->Container->Blob
```
az group deployment create --name deployment --resource-group hackers --template-file resources.json --parameters parameters.json
```