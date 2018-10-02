# 
class A(object):
    def __init__(self,var_a):
        self.var_a = var_a
        self._var_b = "Default_var_b"

    # object var_aa is not defined in __init__, but can be access like object
    @property
    def var_aa(self):
    	return self.var_a

    @property
    def var_bb(self):
    	return self._var_b

    @var_bb.setter
    def var_bb(self, var):
    	self._var_b = var

print('---- start testing ---')
a = A('Variable_a_First')

# access directly
print(a.var_a)
# access via var_aa, but points to the same object. Important is that we are accessing this variable as a variable and not like finction
print(a.var_aa)

#  getattr helps with default valeu of a variable if such is not yet defined
print(getattr(a, 'dd', 'nie ma takiego atrybutu'))
#print(a.dd)

#  Again, there is no var_bb (only var_b), but we can access it as variable
print(a.var_bb)

# but what is more important, we can also change it's value as a variable.
a.var_bb = 'Changed var_bb value'
print(a.var_bb)