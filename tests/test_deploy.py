import pytest

import deploy


@pytest.fixture
def dataset_schema_directory(monkeypatch):
    return monkeypatch.setenv("dataset_schema_directory", "schemas/project")


@pytest.fixture
def gcp_project(monkeypatch):
    return monkeypatch.setenv("gcp_project", "gcp_project")


@pytest.fixture
def credentials(monkeypatch):
    return monkeypatch.setenv("credentials", "{'secret': 'value'}")


def test__validate_env_variables_missing_dataset_schema_directory(
    gcp_project, credentials
):
    with pytest.raises(Exception) as exec_info:
        deploy._validate_env_variables()
    assert exec_info.value.args[0] == "Missing `dataset_schema_directory` config"


def test__validate_env_variables_missing_gcp_project(
    dataset_schema_directory, credentials
):
    with pytest.raises(Exception) as exec_info:
        deploy._validate_env_variables()
    assert exec_info.value.args[0] == "Missing `gcp_project` config"


def test__validate_env_variables_missing_credentials(
    gcp_project, dataset_schema_directory
):
    with pytest.raises(Exception) as exec_info:
        deploy._validate_env_variables()
    assert exec_info.value.args[0] == "Missing `credentials` config"


def test__validate_env_variables_all_variables_present(
    gcp_project, dataset_schema_directory, credentials
):
    deploy._validate_env_variables()
    assert True
