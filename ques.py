#reverse string
n = 'hello world'
print(f'Original String :{n} Reversed String is :{n[::-1]}')

#palindrome
n1 = 'aos'
if n1[::-1] == n1:
    print('Palindrome')
else:
    print('Not a palindrome')

#vovels count
n2 = 'malav'
vovels = 'aeiou'
count = 0
for i in n2:
    if i in vovels:
        count += 1
print(f'Vovels count in {n2} is {count}')

#count words in a string 
n3 = 'hello world'
print(f'Word count are :{len(n3.split())}')

#remove consonants

n4 = 'HelloThere'
vov1 = 'aeiou'
n4 = [i for i in n4 if i in vov1]
print(n4)


