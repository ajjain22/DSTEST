#!/usr/bin/env python3



import math

def minmax(data):
    
    min_=math.inf
    max_=-math.inf
    
    for y in data:
        if y<min_:
            min_=y
        
        elif y>max_:
            max_=y
        
        else:
            print("no change")
    return max_,min_
        
        

def test_type(list_of_int):
    '''
    checks if  min is returned correctly
    '''
    for x in list_of_int:
        
        assert type(x) == type(1), " Following value is not integers :" + str(x)        



def test_max(list_of_int):
    '''
    checks if  max is returned correctly
    '''
    assert max(list_of_int) == minmax(list_of_int)[0], "Function not working as expected"
    

def test_min(list_of_int):
    '''
    checks if  min is returned correctly
    '''
    assert min(list_of_int) == minmax(list_of_int)[1], "Function not working as expected"
    
