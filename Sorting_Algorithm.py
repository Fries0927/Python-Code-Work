import time

def prettyprint(array,colorchange):
    counter = 0
    for i in array:
        for o in colorchange:
            #print(colorchange,counter)
            if counter == o:
                print("\033[33m",end="")
                #print("color")
                break
        print(f"[ {i:^3} ]",end="")
        print("\033[0m",end="")
        counter+=1

def swap(number,element1,element2):
    buffer = number[element1]
    number[element1] = number[element2]
    number[element2] = buffer

def Bubble_Sort(number):
    prettyprint(number,[])
    print("  <<< 初始陣列\n")
    while 1:
        counter = 0
        for i in range(len(number)-1):
            if number[i] > number[i+1]:
                swap(number,i,i+1)
                pprint = [i,i+1]
                prettyprint(number,pprint)
                print("\n")
                counter += 1
                time.sleep(0.5)
        if counter == 0:
            return
        
def Selection_Sort():
    prettyprint(number,[])
    print("  <<< 初始陣列\n")
    for i in range(len(number)):
        smallest = min(number[i:len(number)])
        for o in range(i,len(number)):
            if number[o] == smallest:
                swap(number,i,o)
                break
        pprint = [i,o]
        prettyprint(number,pprint)
        print("\n")
        time.sleep(0.5)

class Insertion_Sort():

    def moveright(o):
        for i in range(len(number)-1,o,-1):
            if number[i] == None:
                number[i] = number[i-1]
                number[i-1] = None
        return i-1

    def Sort():
        buffer = None
        nonepos = None
        prettyprint(number,[])
        print("  <<< 初始陣列\n")
        for i in range(1,len(number)):
            for o in range(i): 
                if number[i] < number[o]:
                    buffer = number[i]
                    number[i] = None
                    nonepos = Insertion_Sort.moveright(o)
                    number[nonepos] = buffer
                    break
                nonepos = i
            pprint = [i,nonepos]
            prettyprint(number,pprint)
            print("\n")
            time.sleep(0.5)

class Merge_Sort():

    @staticmethod
    def merge(list1,list2):
        sorted_list = []
        i,j = 0,0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                sorted_list.append(list1[i])
                i+=1
            else:
                sorted_list.append(list2[j])
                j+=1
        sorted_list.extend(list1[i:])
        sorted_list.extend(list2[j:])
        return sorted_list

    @staticmethod
    def split(array):
        if len(array) == 1:
            return array
        else:
            array1 = array[:len(array)//2]
            array2 = array[len(array)//2:]
            done1 = Merge_Sort.split(array1)
            done2 = Merge_Sort.split(array2)
            if done1 and done2: 
                return Merge_Sort.merge(done1,done2)

    @staticmethod
    def sort(number):
        prettyprint(number,[])
        print("  <<< default list\n")
        if len(number) < 2:
            return
        sorted = Merge_Sort.split(number)
        prettyprint(sorted,[])


class Quick_Sort():

    @staticmethod
    def __pivotHelper(number,min,max):
        if min >= max:
            return

        smaller = min
        pivot = number[(min+max)//2]
        swap(number,(min+max)//2,min)
        ptr = min
        while ptr <= max:
            if number[ptr] < pivot:
                smaller+=1
                swap(number,smaller,ptr)
            ptr+=1
        swap(number,min,smaller)
        Quick_Sort.__pivotHelper(number,min,smaller-1)
        Quick_Sort.__pivotHelper(number,smaller+1,max)

    @staticmethod
    def sort(number): # call this function to trigger quick sort
        prettyprint(number,[])
        print("  <<< default list\n")
        if len(number) < 2:
            return
        Quick_Sort.__pivotHelper(number,0,len(number)-1)
        prettyprint(number,[])

global number

number = []
print("\033[0m",end="")
while True:
    try:
        answer = int(input("輸入數字,然後我會幫你整理好!\n(輸入非數字來停止輸入)\n> "))
        number.append(answer)
    except ValueError:
        break
print("你輸入了",end = "")
for i in number:
    print(f"[ { i : ^ 3} ]",end="")
while 1:
    try:
        answer = int(input("選擇你要看的排序法\n1.泡沫\n2.選擇\n3.插入\n4.合併\n> "))
    except Exception:
        print("請輸入有效的數值!")
        continue
    else:
        if answer == 1:
            Bubble_Sort(number)
        elif answer == 2:
            Selection_Sort()
        elif answer == 3:
            Insertion_Sort.Sort()
        elif answer == 4:
            Merge_Sort.sort(number)
        elif answer == 5:
            Quick_Sort.sort(number)
        else:
            print("請輸入有效的數值!")
            continue
        exit()
