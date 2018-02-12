def palindrome(cadeia):
    if (' ' in cadeia) or (cadeia == "") or (any(char.isdigit() for char in cadeia)): 
        return 'Parametro invalido'

    string_invertida = cadeia[::-1]
    if string_invertida == cadeia:
        return True
    else:
        return False
    
