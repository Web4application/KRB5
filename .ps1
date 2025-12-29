$env:AZURE_DEVOPS_EXT_PAT = $null
$env:AZURE_DEVOPS_EXT_PAT = (Get-Secret "azure-devops-pat")
