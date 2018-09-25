# Azure Upgrade Custom Hackfest
Major challenges facing Azure upgrade. Tackled in order; to help learning and remove technical blockers.

## Outcome
Validation of upgrade to Azure!

## Commands
Login to Azure via CLI
```
az login
```

Set Default Subscription
```
az account set --subscription ""
```

Create Resource Group
```
az group create -g hackers --location "West US 2"
```

Create resource: example for subdirectories
```
az group deployment create \
  --name deployment \
  --resource-group hackers \
  --template-file resources.json \
  --parameters parameters.json
```