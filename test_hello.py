def getItemCount(lst):
  
    count = 0
    for n in lst:
        count += 1        
    return count    

def demo_getItemCount():
    print("Testing hello file code")
    
    #l = (10, 25, 32)
    l = [10, 25, 32,12,5]
    #l = 10
    item_count = getItemCount(l)
    print("Num of items in list = {}".format(item_count))
    
def demos():
    demo_getItemCount()
    

if __name__ == "__main__":
    demos()
