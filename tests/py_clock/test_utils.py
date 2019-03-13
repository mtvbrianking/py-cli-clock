import pytest
from py_clock.utils import get_file_contents

CONTENT = u"Sample read me file."

def test_get_file_contents(readme_file):
    # Write to read me file
    readme_file.write_text(CONTENT)

    # Assert content written to file
    assert readme_file.read_text() == CONTENT

    # Assert that dir contains exactly 1 file
    # readme_file_dir = os.path.dirname(readme_file)
    # # assert len(list(readme_file.iterdir())) == 1

    # Assert util func can read file
    assert get_file_contents(readme_file) == CONTENT
