l1 = [0, 0, 0]
l2 = [55, 220, 156]

def upda(l1,l2):
    for idx,i in enumerate(l1):
        l1[idx] = i+1
        if l1[idx] > l2[idx]:
            l1[idx] = 0
        else: break

upda(l1,l2)
while l1 != [0,0,0]: 
    print(l1)
    upda(l1,l2)