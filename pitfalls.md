# Pitfalls

## Connections to AI models must use KEY authentication for cloud evaluations to succeed
Or else an error may occur, which can be seen from the ml.azure.com studio:
    UserError: load config failed with error Secrets "key" not found in "WorkspaceConnection", please provide the right secret configuration
NOTE: user_logs/std_log.txt is not created in such setup errors

## Automatic retrials upon rate limits
If AI model use runs into rate limits, similar logs may be seen in user_logs/std_log.txt:
INFO:httpx:HTTP Request: POST https://sbn-openai-prod-swc.openai.azure.com/openai/deployments/gpt-4o-auto/chat/completions?api-version=2024-02-15-preview "HTTP/1.1 429 Too Many Requests"
[2025-05-08 09:51:41 +0000][promptflow.core._prompty_utils][ERROR] - Exception occurs: RateLimitError: Error code: 429 - {'error': {'code': '429', 'message': 'Requests to the ChatCompletions_Create Operation under Azure OpenAI API version 2024-02-15-preview have exceeded token rate limit of your current OpenAI S0 pricing tier. Please retry after 50 seconds. Please go here: https://aka.ms/oai/quotaincrease if you would like to further increase the default rate limit. For Free Account customers, upgrade to Pay as you Go here: https://aka.ms/429TrialUpgrade.'}}
[2025-05-08 09:51:41 +0000][promptflow.core._prompty_utils][WARNING] - RateLimitError #1, Retry-After=50, Back off 50.0 seconds for retry.

## AZ credentials
DefaultAzureCredential failed to retrieve a token from the included credentials.
or
CredentialUnavailableError: Failed to invoke the Azure CLI
TODO: az login

# Clean conda environment
conda deactivate
conda remove -n azureai_py3_12 --all
conda create -n azureai_py3_12 python=3.12
NOTE: restart VScode to take effect