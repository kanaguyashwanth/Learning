
'''
Let's take a scenario where your script selects 2 items from the website
- That means the num of items on your cart must be 2, but if that didn't happen,
  then how do we stop the script and make it fail?

  TEST WILL FAIL AND THE SCRIPT WILL BE STOPPED WHERE THERE ARE ERRORS
'''

ItemsInCart = 0     # Initially

# Method 1:
# if ItemsInCart!=2:
#     raise Exception("Product Cart count not matching")


# Method 2: (called as 'Assertion')
'''
Whenever Assert condition is false, it will break the test.
Whenever we see exit code 0, then there are no failures.
'''
if ItemsInCart!=2:
    pass             # pass keyword is to make it do nothing

assert (ItemsInCart == 0)
