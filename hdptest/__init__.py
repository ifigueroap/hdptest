name = "hdptest"

from IPython.core.magic import register_cell_magic
@register_cell_magic
def hdptest(line, cell):
    get_ipython().run_cell_magic('run_pytest[clean]', ' -qq -s --disable-warnings', cell)

del hdptest

@register_cell_magic
def hdptest_io(line, cell):
    get_ipython().run_cell_magic('run_pytest[clean]', ' -qq --capture=sys --disable-warnings', cell)

del hdptest_io


import ipytest
import pytest
ipytest.config(rewrite_asserts=True, magics=True, tempfile_fallback=True)

from .hdptest import hdp_test
from .hdptest import hdp_test_io    

