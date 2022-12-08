nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]
def negative_list(list_of_num):
    neg_list = []
    for num in list_of_num:
        neg_list.append(num * (-1))
    return neg_list

sln1 = negative_list(nums)
print(sln1)

neg = [i * (-1) for i in nums]
print(neg)

sentence2 ="My phone number is (555) 555-4321"
def return_number(string):
    output=[]
    for num in string: 
        if num in "1234567890":
            output.append(num)
    return output

sln2=return_number(sentence2)
print(sln2)

ret = [i for i in sentence2 if i in "1234567890"]
print(ret)

digis = '126'
def digits_plus_uno(digits):
    return str(int(digits)+1)

sln3 = digits_plus_uno(digis)
print(sln3)
