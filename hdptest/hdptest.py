from IPython.core.display import display, HTML
def hdp_test(_fun, _input, _expected):
    try:
        _res = _fun(_input)
        assert _res == _expected
        display(HTML(('<span style="color: green;">Caso de prueba OK!</span>')))
    except:
        display(HTML('<span style="color: red;">Error - se esperaba {0} pero se obtuvo {1}</span>'.format(_expected, _res)))


