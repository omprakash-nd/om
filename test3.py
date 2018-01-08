def changetoint():
    change_list = [10.0, 'chennai', 4.0, 'trichy', 11.0, 'chennai', 5.0, 'trichy', 4.0]
    ls = []
    
    for j in change_list:
        if isinstance(j, float):
            ls.append(int(j))
        else:
            ls.append(j)
    print ls  
    
changetoint()

