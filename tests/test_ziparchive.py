from adelacommon.ziparchive import ZipArchive
from zipfile import ZipFile
import tempfile
import pathlib

def test_addfile(zipdata):
    archive_name = zipdata.get('archive_name')
    y = ZipArchive(archive_name, 'w', verbose=True)
    y.addFile(zipdata.get('file1'), baseToRemove="/tmp")
    y.close()

    with ZipFile(archive_name, 'r') as zf:
        assert pathlib.Path(zipdata.get('file1')).name in zf.namelist()
