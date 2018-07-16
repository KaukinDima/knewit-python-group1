def sum_all(*args, **kwargs):
    print(args)
    print(kwargs)


print(sum_all(123, "hello", one=123, b=45,  var1=98))
