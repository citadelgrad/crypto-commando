import json
from tests.views.test_wallet import test_wallet
import pytest
import shutil


@pytest.fixture(scope="session")
def example_wallet(tmpdir_factory):
    temp_file = tmpdir_factory.mktemp("data").join("test-acc.json")
    shutil.copy("tests/fixtures/test_wallet.json", temp_file)
    return temp_file
