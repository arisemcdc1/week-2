
def input_int (min_, max_):
    while True:
     x = input()    
     if  x.isdigit(): 
       x=int(x)
       if x>= min_ and x<= max_:
        return x    
       else:
        print(" Загаданное число не в интервале")
     else:
            print(" Введите целое число")
print(input_int (30,40))           
