def validador_parenteses(expressao):
    a = 0
    for value in expressao:
        if value == "(" :
            a = a + 1
        else:
            if value == ")" :
                a = a -1
        if a < 0:
            return False
    if a == 0:
        return True
    else:     
        return False
        

