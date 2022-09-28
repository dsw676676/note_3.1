
def change(money,rate,time): # 按年利率的累加折现
    return money/(1+rate)*(1-1/(1+rate))**time/(1-1/(1+rate))

x = (1-2*(1-1/1.08)/(1/1.08*(1-(1/1.08)**10)))/20

print(x)
