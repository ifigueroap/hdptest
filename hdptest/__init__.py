name = "hdptest"

from .hdptest import hdp_test

from IPython.core.magic import register_cell_magic
@register_cell_magic
def hdptest(line, cell):
    get_ipython().run_cell_magic('run_pytest[clean]', ' -qq -s --silent --disable-warnings', cell)

del hdptest

import ipytest
import pytest
ipytest.config(rewrite_asserts=True, magics=True, tempfile_fallback=True);