'''

O(n^2) this is polynomial complexity


'''

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(2)

# Here the loop runs n^2 times so its polynomial