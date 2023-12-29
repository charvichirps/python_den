def getItemCount(lst):
  
    count = 0
    for n in lst:
        count += 1        
    return count    

def demo_getItemCount():
    
    print ("Demo Count Items ")
    
    #l = (10, 25, 32)
    l = [10, 25, 32,12,5]
    #l = 10
    item_count = getItemCount(l)
    print("Num of items in list = {}".format(item_count))
    # count = 0
    # for n in l:
    #     count += 1        
    
    # print("Num of items in list = {}".format(count))
 
def demo_sumItems():
    print ("Demo Sum Items ")
    # step - 1: get a list
    l = [3,4,5]
    # step - 2: iterate over list items and find sum
    sum = 0
    for item in l:
        sum += item
        
    print("Sum = {}".format(sum))
    # step - 3: print sum calculated in step 2
  
        
def demos():
    print("Testing hello file code")    
    demo_getItemCount()
    demo_sumItems()
    # demo_factorial()
    # demo_average()

if __name__ == "__main__":
    demos()
