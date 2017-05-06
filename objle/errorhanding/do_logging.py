import logging
logging.basicConfig(level=logging.INFO)
def foo():
    #s='2'
    s='0'
    n = int(s)
    logging.info('n=%d',n)
    return 10/n
foo()