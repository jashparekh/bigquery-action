import pytest

from plugin_scripts.pipeline_exceptions import (
    DatasetSchemaDirectoryNonExistent,
    DeployFailed,
)


@pytest.mark.parametrize(
    "exception_object",
    [
        DatasetSchemaDirectoryNonExistent({}),
        DeployFailed({}),
    ],
)
def test_exception_init(exception_object):
    e = exception_object
    assert isinstance(e, Exception)


@pytest.mark.parametrize(
    "exception_class",
    [
        DatasetSchemaDirectoryNonExistent,
        DeployFailed,
    ],
)
def test_exception_throws(exception_class):
    e = exception_class({})
    with pytest.raises(exception_class):
        raise e
