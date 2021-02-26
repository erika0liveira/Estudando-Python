import numpy as np

nrand = tuple(np.random.randint(100, size=5))

print('\nOs 5 números gerados para esta lista foram: ', end='')
for i in range(len(nrand)):
    if i == 4:
        print(nrand[i], end='\n')
    else:
        print(nrand[i], end=' ~ ')

print(f'\nO menor número foi: {min(nrand)}')
print(f'O maior número foi: {max(nrand)}')