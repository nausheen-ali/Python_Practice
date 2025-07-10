def list_mult(numbers):
    product=1
    for num in numbers:
        product=product*num
    return product

list1=list(map(int, input("Enter numbers seperated by spaces:").split()))

print("Product of the numbers is:", list_mult(list1))
