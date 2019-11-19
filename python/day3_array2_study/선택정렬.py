def selectionSort(a):
    for i in range(0, len(a)-1):
        min_num = i
        for j in range(i+1, len(a)):
            if a[min_num] > a[j]:
                min_num = j

        a[i], a[min_num] = a[min_num], a[i]

data = [64, 25, 10, 22, 11]
selectionSort(data)
print(data)