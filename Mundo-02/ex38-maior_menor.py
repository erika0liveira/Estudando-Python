nums = list(input('Digite dois números: ').split(' '))

if nums[0] > nums[1]:
    print('\nO primeiro valor digitado {} é maior que o segundo valor {}'.format(nums[0], nums[1]))
elif nums[0] == nums[1]:
    print('\nOs valores {} e {} são iguais'. format(nums[0], nums[1]))
else:
    print('\nO segundo valor digitado {} é maior que o primeiro valor {}'.format(nums[1], nums[0]))
