from IPython.core.display import display, HTML

def hdp_test(_fun, _input, _expected):
    ok__message = '<span style="color: green;"><b>[OK]</b> Caso de prueba correcto para entrada {0}</span>'
    err_message = '<span style="color: red;"><b>[ERROR]</b> Para entrada {0} se espera {1} pero se obtuvo {2}</span>'
    try:
        _res = _fun(_input)
        assert _res == _expected
        display(HTML(ok__message.format(_input)))
    except:
        display(HTML(err_message.format(_input, _expected, _res)))


