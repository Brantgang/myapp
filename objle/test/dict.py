class Dict(dict):

    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, key):
         try:
             return self[key]
         except KeyError:
             raise AttributeError(r"'dict' object has no atribute '%s'"%key)



    def __setattr__(self, key, value):
        self[key]=value