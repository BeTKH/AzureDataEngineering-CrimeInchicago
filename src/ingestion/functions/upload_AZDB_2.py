import os
import requests
import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient


def init_storage_acct(storage_account_name, storage_account_key):
    """Initialize the Azure Data Lake service client."""
    service_client = DataLakeServiceClient(account_url=f"https://{storage_account_name}.dfs.core.windows.net",
                                           credential=storage_account_key)
    return service_client


# def createAzContainer(service_client, file_system_name):
#     """Create a file system (container) in the Azure Data Lake."""
#     file_system_client = service_client.create_file_system(
#         file_system=file_system_name)
#     print(f"Container '{file_system_name}' created successfully.")
#     return file_system_client


# def create_directory(file_system_client, directory_name):
#     """Create a directory inside the file system."""
#     directory_client = file_system_client.create_directory(directory_name)
#     print(f"Directory '{directory_name}' created successfully.")
#     return directory_client


def upload_dataframe_to_adls(directory_client, df, remote_file_name):
    """Upload a DataFrame as a CSV file to Azure Data Lake."""

    if not remote_file_name.endswith('.csv'):
        remote_file_name += '.csv'

    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)

    # Create a file client in the specified directory
    file_client = directory_client.create_file(remote_file_name)

    # Upload the CSV data
    file_client.upload_data(csv_data, overwrite=True)
    print(f"DataFrame uploaded as '{remote_file_name}' successfully.")
