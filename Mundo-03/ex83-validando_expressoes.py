exp = list(input('Digite a expressão: '))
paren = []
for i in exp:
    if i == '(':
        paren.append('(')
    elif i == ')':
        if len(paren) > 0:
            paren.pop()
        elif len(paren) < 1:
            paren.append(')')
if not paren:
    print('\nExpressão válida')
else:
    print('\nExpressão não é válida')
