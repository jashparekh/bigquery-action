[![Actions Status](https://github.com/jashparekh/bigquery-action/workflows/Lint/badge.svg?branch=main)](https://github.com/jashparekh/bigquery-action/actions)
[![Actions Status](https://github.com/jashparekh/bigquery-action/workflows/Unit%20Tests/badge.svg?branch=main)](https://github.com/jashparekh/bigquery-action/actions)
[![Actions Status](https://github.com/jashparekh/bigquery-action/workflows/Integration%20Test/badge.svg?branch=main)](https://github.com/jashparekh/bigquery-action/actions)
![Version](https://img.shields.io/static/v1.svg?label=Version&message=v1&color=lightgrey&?link=http://left&link=https://github.com/jashparekh/bigquery-action/tree/v1)


# BigQuery Github Action

This Github action can be used to deploy tables/views schemas to BigQuery.

### Simple

```yaml
name: "Deploy to BigQuery"
on:
  pull_request: {}
  push:
      branches: ["main"]

jobs:
  deploy_schemas:
    runs-on: ubuntu-latest
    name: Deploy to BigQuery
    steps:
      # To use this repository's private action,
      # you must check out the repository
      - name: Checkout
        uses: actions/checkout@v2
      - name: Deploy schemas to BigQuery
        uses: jashparekh/bigquery-action@v1
        env:
          gcp_project: 'gcp-us-project'
          dataset_schema_directory: 'gcp-us-project/dataset_name'
          credentials: ${{ secrets.GCP_SERVICE_ACCOUNT }}
```

## Configuration

### Required

### `gcp_project` (required, string)

The full name of the GCP project you want to deploy.

Example: `gcp-us-project`

### `dataset_schema_directory` (required, string)

The directory in your repository where are you storing the schemas for your tables and views.

Example: `gcp-us-project/dataset_name`

### `credentials` (required, string)

Google Service Account with permission to create objects in the specified project. Can be stored as a [repository secret](https://docs.github.com/en/actions/reference/encrypted-secrets)

## Schemas

This action uses [GBQ](https://github.com/wayfair-incubator/gbq) to deploy to Google BigQuery.
[GBQ](https://github.com/wayfair-incubator/gbq) now supports specifying partitions with the schema as well.

To leverage this you need to nest your JSON table schema in a dictionary. An example for the same is given below. Library supports Time and Range based partitioning along with Clustering.

All the configuration options can be found [here](https://github.com/wayfair-incubator/gbq/blob/main/gbq/dto.py).

```json
{
  "partition": {
    "type": "range",
    "definition": {
      "field": "ID",
      "range": {
        "start": 1,
        "end": 100000,
        "interval": 10
      }
    }
  },
  "clustering": [
    "ID"
  ],
  "schema": [
    {
      "name": "ID",
      "type": "INTEGER",
      "mode": "REQUIRED"
    }
  ]
}
```

## Contributing

See the [Contributing Guide](CONTRIBUTING.md) for additional information.

To execute tests locally (requires that `docker` and `docker-compose` are installed):

```bash
docker-compose run test
```

## Credits

This Github Action was originally written by [Jash Parekh](https://github.com/jashparekh).
