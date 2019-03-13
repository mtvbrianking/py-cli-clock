import pytest
from py_clock.utils import get_file_contents

CONTENT = u"Sample read me file."

def test_get_file_contents(tmpdir):
    tmp_file = tmpdir.mkdir("py_clock").join("README.md")
    tmp_file.write(CONTENT)
    # Assert content written
    assert tmp_file.read() == CONTENT
    # Assert dir has exactly 1 file
    assert len(tmpdir.listdir()) == 1
    # Assert util func can read file
    assert get_file_contents(tmp_file) == CONTENT
