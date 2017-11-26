import os
from six.moves.urllib.request import urlretrieve
import tensorflow as tf
import zipfile
def maybe_download(url, filename, expected_bytes):
  """Download a file if not present, and make sure it's the right size."""
  if not os.path.exists(filename):
    filename, _ = urlretrieve(url + filename, filename)
  statinfo = os.stat(filename)
  if statinfo.st_size == expected_bytes:
    print('Found and verified %s' % filename)
  else:
    print(statinfo.st_size)
    raise Exception(
      'Failed to verify ' + filename + '. Can you get to it with a browser?')
  return filename


def read_data(filename):
  """read data from a file on disk."""
  with zipfile.ZipFile(filename) as f:
    for name in f.namelist():
      return tf.compat.as_str(f.read(name))


