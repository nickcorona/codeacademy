def middle_element(lst):
    length = len(lst)
    mid = int(length / 2)
    if length % 2 == 0:
        mid_lst = lst[mid - 1: mid + 1]
        mid_avg = sum(mid_lst) / 2
        return mid_avg
    else:
        mid_element = lst[mid]
        return mid_element

