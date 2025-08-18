from testbook import testbook
import numpy as np

def test_cleaning():
    with testbook('1_data_cleaning.ipynb', execute=True) as tb:
        mean_temperature = tb.ref('mean_temperature')
        assert np.isclose(mean_temperature, 25.157, atol=1e-3)