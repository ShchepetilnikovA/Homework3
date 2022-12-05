lst = []


def nego_fibonacci(count):
    
    
    def nego (num1, num2, count):
        if count > 1:
            temp = num1
            num1 = num2
            num2 = temp - num2
            nego(num1, num2, count - 1)
            lst.append(num2)
    
    
    nego(0, 1, count)
    lst.append(int(1))
    lst.append(int(0))
    lst.append(int(1))
    
    
    def fibonacci(count):
        for i in range(count + 1, count * 2):
            lst.append(lst[i] + lst[i - 1])
    
    
    fibonacci(count)
    

nego_fibonacci(int(input('input amount of elements in negofibonacci: ')))
print(lst)