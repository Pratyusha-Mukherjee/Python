def secondlarge(arr, arr_size):
        
        arr.sort()
        for i in range (1,arr_size): 
            print(arr[i],end=" ")
        print("\n")
        arr.reverse()
        for i in range(1,arr_size): 
            print(arr[i],end=" ")   
        print("\nThe second largest element is ",arr[2])       


array = [5,1,4,6,24,12,20,90]
n = len(array)
secondlarge(array,n)
   

  