# Using Mutable objests as default arguments
def update_order(new_item, current_order=[]):
    current_order.append(new_item)
    return current_order

# First order, burger
order1 = update_order({'item':'buger', 'cost': '3.50'})

# Second order, just a soda
order2 = update_order({'item':'soda', 'cost':'1.50'})

#what's in that second order again
print(order2)
'''
official python documentation on function defination.
Default parameter values are evaluated from left to right when the function definition is executed. 
This means that the expression is evaluated once, when the function is defined, and that the same 
“pre-computed” value is used for each call.
This means that when we call a function, the default values we provide for parameters are only 
created once, and used for each subsequent call of the function. This means our grades=[] 
from our earlier function was only created once and anytime we tried to access it, 
the same list was being modified. We can even see that the memory id of the grades 
property for both students is the same (using the built-in id() function):
'''
print(id(order1))
print(id(order2))

