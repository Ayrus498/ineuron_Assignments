# Logic function
def Assignment1():
    divisible_by = 7
    multiple_by = 5

    for i in range(2000,3200):
        if((i % divisible_by) == 0) and ((i % multiple_by) !=0):
            print(i,end = ",")  

Assignment1()