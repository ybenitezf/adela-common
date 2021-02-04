import pytest
import tempfile
import shutil
import os

@pytest.fixture
def zipdata():
    """Create a dir and some simple files"""
    workdir = tempfile.mkdtemp()
    dir1 = tempfile.mkdtemp()
    dir2 = tempfile.mkdtemp()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        archive_name = f.name
    with tempfile.NamedTemporaryFile(delete=False) as f:
        file1 = f.name
        f.write(b"Hello from pytest!\n")
    data = {
        'workdir': workdir,
        'dir1': dir1,
        'dir2': dir2,
        'file1': file1,
        'archive_name': archive_name
    }
    yield data
    os.unlink(file1)
    os.unlink(archive_name)
    shutil.rmtree(dir1, ignore_errors=True)
    shutil.rmtree(dir2, ignore_errors=True)
    shutil.rmtree(workdir, ignore_errors=True)
