import array
import random

def triangular(n):
    return (n+1) * n // 2

def sortbubble(arr):
    print(f'{arr} initial array')
    tswap = 0
    for i in range(len(arr)-1):
        print(f'start loop {i}')
        nswap = 0
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                nswap += 1
                print(f'{arr} swapped position {j-1} and {j}')
        print(f'ncomp == {len(arr)-1-i}, nswap == {nswap}, end loop {i}')
        if nswap == 0:
            break
        tswap += nswap
    print(f'{arr} tcomp == {triangular(len(arr)-1) - triangular(len(arr)-i-2)}, tswap == {tswap}, final array')

def sortinsertion(arr):
    print(f'{arr} initial array')
    tcomp, tswap = 0, 0
    for i in range(len(arr)-1):
        print(f'start loop {i}')
        ncomp, nswap = 0, 0
        for j in range(i+1, 0, -1):
            ncomp += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                nswap += 1
                print(f'{arr} swapped position {j-1} and {j}')
            else:
                break
        print(f'ncomp == {ncomp}, nswap == {nswap}, end loop {i}')
        tcomp += ncomp
        tswap += nswap
    print(f'{arr} tcomp == {tcomp}, tswap == {tswap}, final array')

def sortexchange(arr):
    print(f'{arr} initial array')
    tswap = 0
    for i in range(len(arr)-1):
        print(f'start loop {i}')
        nswap = 0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                nswap += 1
                print(f'{arr} swapped position {i} and {j}')
        print(f'ncomp == {len(arr)-i-1}, nswap == {nswap}, end loop {i}')
        tswap += nswap
    print(f'{arr} tcomp == {triangular(len(arr)-1)}, tswap == {tswap}, final array')

def sortselection(arr):
    print(f'{arr} initial array')
    tswap = 0
    for i in range(len(arr)-1):
        print(f'start loop {i}')
        minindex = i
        nswap = 0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        if minindex != i:
            arr[i], arr[minindex] = arr[minindex], arr[i]
            nswap += 1
            print(f'{arr} swapped position {i} and {minindex}')
        print(f'ncomp == {len(arr)-i-1}, nswap == {nswap}, end loop {i}')
        tswap += nswap
    print(f'{arr} tcomp == {triangular(len(arr)-1)}, tswap == {tswap}, final array')

arr = array.array('b', range(7))

random.Random(0).shuffle(arr)
sortbubble(arr)

random.Random(0).shuffle(arr)
sortinsertion(arr)

random.Random(0).shuffle(arr)
sortexchange(arr)

random.Random(0).shuffle(arr)
sortselection(arr)
