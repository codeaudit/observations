from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.survival import survival


def test_survival():
  """Test module survival.py by downloading
   survival.csv and testing shape of
   extracted data has 14 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = survival(test_path)
  try:
    assert x_train.shape == (14, 2)
  except:
    shutil.rmtree(test_path)
    raise()
