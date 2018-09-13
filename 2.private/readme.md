# Azure VNet Setup

## Issues
1. Validate components to deploy
2. Ensure all systems are secured within the VNet

## Outcome
Have a couple of compute resources, storage and database (Postgres/Cosmos DB) that can privately interact with each other.

## How to deploy
1. Create a resource group
```bash
az group create -g uhackfest2
```
1. Deploy the template
```bash
az group deployment create\
    -g uhackfest2\
    --n uhackfestdeployment\
    --template-file azuredeploy.json\
    --parameters dnsPrefixForPublicIP=uhackfest
```