# airflow-compose

docker-compose project to create a local airflow deployment with Azure Active Directory authentication enabled

## Start

- Execute `./ad-app/create-ad-app.sh your-application`. This script registers an application with name `your-application` in Azure AD with:
    - delegated permissions for `openid` and `profile`
    - additional claim `upn`. By default Azure AD application is not returning this claim, which is required by airflow
    - add application secret
- Note down application id and password from output of script above
- Create a file `oauth-secrets.env` file at the root folder with content:

```
AZURE_APPLICATION_ID=application-id-from-step-1
AZURE_SECRET=password-from-step-1
AZURE_TENANT_ID=tenant-id-from-azure-ad
```

- Run `docker-compose up -d`
- Go to `http://localhost:8080`, click `Register` and log in with your Azure AD account
