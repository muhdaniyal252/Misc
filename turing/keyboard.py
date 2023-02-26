
def entryTime(s, keypad):
    list1 = list(keypad[:3])
    list2 = list(keypad[3:6])
    list3 = list(keypad[6:])
    seconds = list()
    i = s[0]
    if i in list1:
        current_list = 1
        current_position = list1.index(i)
    if i in list2:
        current_list = 2
        current_position = list2.index(i)
    if i in list3:
        current_list = 3
        current_position = list3.index(i)
    for i in s[1:]:
        if i in list1:
            list_diff = abs(current_list-1)
            pos_diff = abs(current_position-list1.index(i))
            current_list = 1
            current_position = list1.index(i)
        elif i in list2:
            list_diff = abs(current_list-2)
            pos_diff = abs(current_position-list2.index(i))
            current_list = 2
            current_position = list2.index(i)
        elif i in list3:
            list_diff = abs(current_list-3)
            pos_diff = abs(current_position-list3.index(i))
            current_list = 3
            current_position = list3.index(i)
        seconds.append(list_diff)
        if list_diff == 0:
            pos_diff = pos_diff
        elif list_diff == 1 and pos_diff == 2:
            pos_diff == 1
        elif list_diff == 2:
            pos_diff == 0
        seconds.append(pos_diff)
    return sum(seconds)
