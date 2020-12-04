from timeit import default_timer as timer
PI = 3
working = []
num = 600851475143
start = timer()

while(num != 1):                    
    PI = PI + 2                     
    divisoren = 0                     
    divisor = 1                    
    
    while divisor <= PI:
        if PI % 3 == 0 and PI != 3:
            break
        if PI % 5 == 0 and PI != 5:
            break
        if PI % 7 == 0 and PI != 7:
            break
        if PI % 11 == 0 and PI != 11:
            break                  
        if PI % divisor == 0:       
            divisor += 1           
            divisoren += 1           
        else:
            divisor += 1            
        
        if divisoren == 2:         
            if num % PI == 0:       
                num = num // PI     
                working.append(PI) 
                print(working)     
                if num == 1:       
                    print(working) 
end = timer()
print(end-start)
