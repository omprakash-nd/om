def destination():
    traindept = [[13, 'chn', 18, 'tcy'],[13, 'tcy', 21, 'mdu'],[19, 'tcy', 23, 'mdu'],[21, 'chn', 18, 'vij']]
    ss = [23,'chn','mdu']
    dest =[]
    for i in range(len(traindept)):
        if traindept[i][1] == ss[1]:
            if traindept[i][3] == ss[2]:
                if ss[0] == traindept[i][0] or ss[0] <= traindept[i][0] :
                    print traindept[i]
            elif traindept[i][3] != ss[2]:
                dest.append((traindept[i][3],traindept[i][2]))
                #dest.append()
            
    print dest                
                
destination()
