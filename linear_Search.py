pos=-1


def search(list,n):


    for i in range(6):
        if list[i]==n:
            globals() ['pos'] = i+1
            return True
        i+=1





list = [12,33,34,55,62,71]
n= 22



if search(list,n):
    print("Found",pos)
else:
    print("not found")