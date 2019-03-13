# contents of conftest.py
import pytest

@pytest.fixture()
def readme_file(tmp_path):
    # Create temp file
    sub_dir = tmp_path / "py_clock"
    sub_dir.mkdir()
    return sub_dir / "README.md"
