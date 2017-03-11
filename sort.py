def bubble_sort(l):
    did_swaps = True
    pass_num = len(l)-1
    while did_swaps and pass_num > 0:
        did_swaps = False
        for ii in range(pass_num):
            if l[ii] > l[ii+1]:
                did_swaps = True
                l[ii], l[ii+1] = l[ii+1], l[ii]
        pass_num -= 1
    return l

def selection_sort(l):
    for ii in range(len(l)-1):
        min_value = l[ii]
        min_idx = ii
        for jj in range(ii+1,len(l)):
            if l[jj] < min_value:
                min_value = l[jj]
                min_idx = jj
        l[ii], l[min_idx] = l[min_idx], l[ii]
        print(l)

def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        new_l = []
        left = merge_sort(l[:len(l)//2])
        right = merge_sort(l[len(l)//2:])
        while left and right:
            if left[0] < right[0]:
                new_l.append(left.pop(0))
            else:
                new_l.append(right.pop(0))
        for i in left:
            new_l.append(left.pop(0))
        for i in right:
            new_l.append(right.pop(0))
        return new_l

def quick_sort(l):
    def sort_func(l, low, high):
        if high-low > 1:
            pivot = l[low]
            left_cursor = low+1
            right_cursor = high
            while left_cursor < right_cursor:
                if l[left_cursor] <= pivot:
                    left_cursor += 1
                elif l[right_cursor] > pivot:
                    right_cursor -= 1
                else:
                    l[left_cursor], l[right_cursor] = l[right_cursor], l[left_cursor]
            if pivot > l[left_cursor]:
                pivot_swap = left_cursor
            else:
                pivot_swap = left_cursor - 1
            l[low], l[pivot_swap] = l[pivot_swap], l[low]
            sort_func(l, low, pivot_swap-1)
            sort_func(l, pivot_swap+1, high)
    sort_func(l,0,len(l)-1)
    return l
