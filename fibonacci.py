# the first numbers for fibonacci series
prev2 = 0 
prev1 = 1

print(prev2)
print(prev1)

for i in range(18):
    newFib = prev2 + prev1
    print(newFib)
    prev2 = prev1
    prev1 = newFib

print('\n' 'Done')

# recvursive method
