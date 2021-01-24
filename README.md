# airflow-compose

docker-compose project to create a local airflow deployment with Azure Active Directory authentication enabled

## Start

- Register an application in Azure AD
- Add `upn` to the application `Token configuration`
- Create a file `oauth-secrets.env` file at the root folder with content:

```
AZURE_APPLICATION_ID=client-id-from-azure-ad
AZURE_SECRET=client-secret-from-azure-ad
AZURE_TENANT_ID=tenant-id-from-azure-ad
```

- Run `docker-compose up -d`
- Go to `http://localhost:8080`, click `Register` and log in with your Azure AD account
