name = "John"
age = 24
print("My name is %s and my age is %d" % (name, age))

a_list = [1, 2, 3, 4, 5]
print("list: %s" % (a_list))

a_list = (1, 2, 3, 4, 5)
print("Tuple: %s %s %s %s %s" % (a_list))

try:
    a_list = [1, 2, 3, 4, 5]
    print("list: %s %s %s %s %s" % (a_list))    
except Exception:
    print("Error:  List [1, 2, 3, 4, 5] cannot be used as 'list: %s %s %s %s %s ' List can be represented by only one symbol")



# Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%4.2f"

print(format_string % data)






#  USING PyFORMAT
print('PyFormat Library'.center(50,'-'))
'''
SYMBOLS:

%d - Integer
%s - String
%r - Repr
%a - 

'''

print('BASIC FORMATTING'.center(50,'-'))

print('%s %s' %('one','two'))                       #OLD
print('{} {}'.format('one','two'))                  #NEW

print('%d %d' %(1,2))                               #OLD
print('{} {}'.format(1,2))                          #NEW

# Here we are explicitly specifying which var to take.
print('{1} {0}'.format('one','two'))                #NEW

print('VALUE CONVERSION'.center(50,'-'))

class Data(object):
    def __str__(self):
        return 'str'
    
    def __repr__(self):
        return 'repr'

print('%s %r' %(Data(), Data()))                    #OLD
print('{0!s} {0!r}'.format(Data()))                 #NEW


class DataB(object):

    def __repr__(self):
        return 'räpr'

print('%r %a' % (DataB(),DataB()))
print('{0!r}  {0!a}'.format(DataB()))
# OUTPUT - räpr r\xe4pr

print('PADDING AND ALIGNING STRINGS'.center(50,'-'))

print('ALIGN RIGHT')
print('%10s' % ('test'))                            #OLD
print('{:>10}'.format('test'))                      #NEW
# OUTPUT - '      test'

print('{:_>10}'.format('test'))                     #NEW
# OUTPUT - '______test'

print('ALIGN LEFT')
print('%-10s' %('test'))                            #OLD
print('{:<10}'.format('test'))                      #NEW
# OR print('{:10}'.format('test'))                  #NEW
# OUTPUT - 'test      '

print('{:_<10}'.format('test'))                     #NEW
# OUTPUT - 'test______'

print('CENTER')
print('{:^10}'.format('test'))                      #NEW
# OUTPUT - '   test   '
print('{:_^10}'.format('test'))                     #NEW
# OUTPUT - '___test___'

print('TRUNCATING LONG STRINGS'.center(50,'-'))

print('%.5s' % ('xylophone'))
print('{:.5}'.format('xylophone'))
# OUTPUT - 'xylop'

print('%-10.5s' % ('xylophone'))
print('{:10.5}'.format('xylophone'))
# OUTPUT - 'xylop     '

print('NUMBERS'.center(50,'-'))

print('%d' %(42))
print('{:d}'.format(42))
# print('{:d}'.format('Forty'))




