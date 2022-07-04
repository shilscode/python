from dataclasses import replace


def rep(p):
    s= p[0]
    st= p.replace(s,'$')
    
    print (s+ st[1:])
rep('wwww')
    



