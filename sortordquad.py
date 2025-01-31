import array
import random

def sortbubble(arr):
    print(f'{arr} initial')
    for sublength in range(len(arr), 1, -1):
        swapcount = 0
        print(f'sublength {sublength} start')
        for i in range(sublength-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapcount += 1
                print(f'{arr} swap {i} {i+1}')
        if swapcount == 0:
            print(f'swapcount {swapcount} break end')
            break
        else:
            print(f'swapcount {swapcount} end')
    print()

def sortinsertion(arr):
    print(f'{arr} initial')
    for sublength in range(len(arr), 1, -1):
        swapcount = 0
        print(f'sublength {sublength} start')
        for i in range(sublength-2, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapcount += 1
                print(f'{arr} swap {i} {i+1}')
            else:
                break
        print(f'swapcount {swapcount} end')
    print()

def sortexchange(arr):
    print(f'{arr} initial')
    for sublength in range(len(arr), 1, -1):
        swapcount = 0
        print(f'sublength {sublength} start')
        for i in range(sublength-1):
            if arr[i] > arr[sublength-1]:
                arr[i], arr[sublength-1] = arr[sublength-1], arr[i]
                swapcount += 1
                print(f'{arr} swap {i} {sublength-1}')
        print(f'swapcount {swapcount} end')
    print()

def sortselection(arr):
    print(f'{arr} initial')
    for sublength in range(len(arr), 1, -1):
        maxindex = sublength - 1
        indexswapcount = 0
        print(f'sublength {sublength} start')
        for i in range(sublength-1):
            if arr[i] > arr[maxindex]:
                maxindex = i
                indexswapcount += 1
                print(f'maxindex {maxindex}')
        if indexswapcount != 0:
            arr[maxindex], arr[sublength-1] = arr[sublength-1], arr[maxindex]
            print(f'{arr} swap {sublength-1} {maxindex}')
        print(f'indexswapcount {indexswapcount} end')
    print()

arr = array.array('b', range(7))

random.Random(0).shuffle(arr)
sortbubble(arr)

random.Random(0).shuffle(arr)
sortinsertion(arr)

random.Random(0).shuffle(arr)
sortexchange(arr)

random.Random(0).shuffle(arr)
sortselection(arr)
