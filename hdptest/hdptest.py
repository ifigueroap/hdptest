from IPython.core.display import display, HTML

def hdp_test(_fun, _expected, *_input):
    ok__message = '<span style="color: green;"><b>[OK]</b> Caso de prueba correcto para entrada {0}</span>'
    err_message = '<span style="color: red;"><b>[ERROR]</b> Para entrada {0} se espera {1} pero se obtuvo {2}</span>'
    try:
        _res = _fun(*_input)
        assert _res == _expected
        display(HTML(ok__message.format(_input)))
    except:
        display(HTML(err_message.format(_input, _expected, _res)))

import re
def compare_ignore_spaces(a, b):
    """
    Compare two base strings, disregarding whitespace
    """
    return re.sub("[\n\t\s]*", "", a) == re.sub("[\n\t\s]*", "", b)

import sys
from unittest.mock import patch

def hdp_test_io(capsys, _fun, _expected_output, user_input = [], *_input):
    """
    Función especializada para hacer pruebas en base a la entrada del usuario
    y el texto de salida por pantalla, por ejemplo usando print.
    Si _expected no es None, también se prueba que la función produzca el valor esperado.

    Para usarse en el contexto de hdptest es necesario crear una función test_X(capsys)
    que incorpore el fixture capsys, provisto por pytest para capturar la salida por pantalla.
    
    Es decir, algo como:
        def test_X(capsys):
            hdp_test_io(capsys, ...)    
    """

    ok__message = '<span style="color: green;"><b>[OK]</b> Caso de prueba correcto para entrada {0}</span>'
    err_message = '<span style="color: red;"><b>[ERROR]</b> Para entrada {0} se espera que se imprimiera {1}</span>'
        
    with patch('builtins.input', side_effect=user_input):
        _fun(*_input)
        out, _ = capsys.readouterr()
        with capsys.disabled():
            sys.stdout.write(out)        
        try:    
            assert compare_ignore_spaces(out, _expected_output)
            display(HTML(ok__message.format(user_input)))
        except:
            display(HTML(err_message.format(user_input, _expected_output)))
    