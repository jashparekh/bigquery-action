import json
import os
import sys

from gbq import BigQuery

sys.tracebacklimit = 0


def _validate_env_variables():
    if not os.environ.get("gcp_project"):
        raise Exception("Missing `gcp_project` config")

    if not os.environ.get("dataset_schema_directory"):
        raise Exception("Missing `dataset_schema_directory` config")

    if not os.environ.get("credentials"):
        raise Exception("Missing `credentials` config")


def _deploy():
    dataset_schema_directory = os.environ.get("dataset_schema_directory")
    credentials = os.environ.get("credentials")
    gcp_project = os.environ.get("gcp_project")

    try:
        bq = BigQuery(credentials, gcp_project)
        for root, dirs, files in os.walk(dataset_schema_directory):
            dataset = root.split("/").pop()
            for file in files:
                with open(f"{root}/{file}", "r") as contents:
                    file_name_and_extension = file.split(".")
                    print(
                        f"Updating schema for {gcp_project}.{dataset}.{file_name_and_extension[0]}"
                    )
                    if file_name_and_extension[1] == "sql":
                        schema = contents.read()
                        bq.create_or_update_view(
                            gcp_project, dataset, file_name_and_extension[0], schema
                        )
                    else:
                        schema = json.loads(contents.read())
                        bq.create_or_update_structure(
                            gcp_project, dataset, file_name_and_extension[0], schema
                        )
    except Exception as e:
        print(f"Failed to deploy to Bigquery: {e}")


if __name__ == "__main__":
    _validate_env_variables()
    _deploy()
