def is_valid_IP(strng):
    return None


#  valid inputs:
# 1.2.3.4
# 123.45.67.89

#  invalid inputs:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

print(is_valid_IP('12.255.56.1'),     True)
print(is_valid_IP(''),                False)
print(is_valid_IP('abc.def.ghi.jkl'), False)
print(is_valid_IP('123.456.789.0'),   False)
print(is_valid_IP('12.34.56'),        False)
print(is_valid_IP('12.34.56 .1'),     False)
print(is_valid_IP('12.34.56.-1'),     False)
print(is_valid_IP('123.045.067.089'), False)
print(is_valid_IP('127.1.1.0'),        True)
print(is_valid_IP('0.0.0.0'),          True)
print(is_valid_IP('0.34.82.53'),       True)
print(is_valid_IP('192.168.1.300'),   False)


def move_zeros(array):
    pass
    #your code here

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

print(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
print(move_zeros(["a","b"]),["a","b"])
print(move_zeros(["a"]),["a"])
print(move_zeros([0,0]),[0,0])
print(move_zeros([0]),[0])
print(move_zeros([]),[])