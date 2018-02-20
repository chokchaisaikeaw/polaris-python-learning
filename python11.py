seqlist=list(range(0,100))
for seq in seqlist:
    if seq%10 == 1:
        print (str(seq)+'st')
    elif seq%10 == 2:
        print (str(seq)+'nd')
    elif seq%10 == 3:
        print (str(seq)+'rd')
    else:
        print (str(seq)+'th')

