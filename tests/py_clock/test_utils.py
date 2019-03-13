import pytest
from py_clock.utils import get_file_contents

CONTENT = u"Sample read me file."

def test_get_file_contents(tmp_path):
    # Create temp file
    sub_dir = tmp_path / "py_clock"
    sub_dir.mkdir()
    tmp_file = sub_dir / "README.md"
    tmp_file.write_text(CONTENT)
    assert tmp_file.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1

    # Assert util func can read file
    assert get_file_contents(tmp_file) == CONTENT
