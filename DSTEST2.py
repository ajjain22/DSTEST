


strings=['shru', 'shruti', 'shm', 'shloow']


def edit_distance(string1, string2):
    
    if len(string1) > len(string2):
        difference = len(string1) - len(string2)
        
        string1=string1[:-difference]

    elif len(string2) > len(string1):
        difference = len(string2) - len(string1)
        string2=string2[:-difference]

    else:
        difference = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            difference += 1
    
            

    return difference




def dist_matrix(strings):
    distance={}
    for i in strings:
        for y in strings:
            distance[(i,y)]=edit_distance(i,y)
        
    
    
res = {key: distance[key] for key in distance.keys() if distance[key]<2}
                                
  








