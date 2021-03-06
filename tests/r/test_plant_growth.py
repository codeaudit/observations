from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.plant_growth import plant_growth


def test_plant_growth():
  """Test module plant_growth.py by downloading
   plant_growth.csv and testing shape of
   extracted data has 30 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = plant_growth(test_path)
  try:
    assert x_train.shape == (30, 2)
  except:
    shutil.rmtree(test_path)
    raise()
