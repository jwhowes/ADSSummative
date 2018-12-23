def MergeSelectionSort(A):
    if len(A) <= 4:
        return SelectionSort(A)
    middle = int(len(A) / 2)
    left = A[0:middle]
    right = A[middle:len(A)]
    return Merge(MergeSelectionSort(left), MergeSelectionSort(right))

def Merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result = result + left
            left = []
        else:
            result = result + right
            right = []
    return result

def SelectionSort(A):
    for i in range(0, len(A) - 1):
        largest = i
        for j in range(i + 1, len(A)):
            if A[j] > A[largest]:
                largest = j
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
    return A
