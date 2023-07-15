# -*- coding: UTF-8 -*-
orig_print=print
def alter_print(*args,**kwargs):
	kwargs['flush']=True
	orig_print(*args,**kwargs)
print=orig_print



