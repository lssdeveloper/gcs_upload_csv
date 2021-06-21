#!/usr/bin/python
# -*- coding: utf-8 -*-

# ==============================================================================
#            U P L O A D   C S V   T O   G O O G L E   S T O R A G E
# ==============================================================================


import os

from google.cloud import storage


def run_quickstart():
    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = "my-ml-projects"

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print("Bucket {} created.".format(bucket.name))


def upload_csv():
    """Uploads a file to the bucket"""
    source_file_name = '/data/'
    files = os.listdir(source_file_name)

    # Setting credentials using JSON file
    storage_client = storage.Client()
    # Getting bucket object
    bucket = storage_client.bucket("my-bigdata-projects")
    for file in files:
        # Name of the object to be stored in the bucket
        object_name_in_gcs_bucket = bucket.blob(f"data/csv/{file}")
        # Uploading from a local file using open()
        with open(source_file_name + file, 'rb') as f:
            object_name_in_gcs_bucket.upload_from_file(f)
        # Uploading from local file without open()
        object_name_in_gcs_bucket.upload_from_filename(source_file_name + file)
        print(
            "File {} uploaded to {}.".format(file, object_name_in_gcs_bucket)
        )


if __name__ == "__main__":
    # run_quickstart()
    upload_csv()
