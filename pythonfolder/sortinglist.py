#sorting a python list.Its compring the item with next to and if the first one is bigger it'll be appended in the end of the list.
#and will be deletd from past position.
list=[4,3,1,5,2]
control=0
while True:
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
         #code that slide the list items and remove the list item which has index i
            list.append(list[i])
            list.remove(list[i])
            print(list)
            break#this break will be execute the inner lopp which is for loop
    control=0
    for k in range(len(list)-1):#approving if the list is sorted or not
        if list[k]<list[k+1]:
            control=control+1
    if control==len(list)-1:
        break
