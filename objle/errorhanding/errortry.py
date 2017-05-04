import logging


try:
    print('try .......')
    r=10/2
    print('result is :',r)
except ValueError as e:
    print('except is :',e)
except ZeroDivisionError as e:
    print('except is :',e)
else:
    print('no error')
finally:
    print('finally......')
print('End')


def boo(s):
    return 10/int(s)

def bar(s):
    return boo(s) * 2


def main():
    try:
         print(bar('0'))
    except ZeroDivisionError as e:
        logging.exception(e)
    finally:
        print('end')


main()


