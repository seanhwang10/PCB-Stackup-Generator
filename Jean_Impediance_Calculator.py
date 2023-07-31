import math

h = 2.7
e_r = 3.5
w = 5
s = 8
t = 1.2

n_0 = 376.73

w_eff = w + (t/math.pi)*math.log((4*math.e)/math.sqrt(((t/h)**2) + ((t/(w*math.pi + 1.1*t*math.pi))**2))) * ((e_r + 1)/(2*e_r))           # 2
x_1 = 4 * ((14*e_r+8)/(11*e_r)) * (h/w_eff)                                                                                               # 3
x_2 = math.sqrt(16 * ((h/w_eff)**2) * (((14*e_r+8)/(11*e_r))**2) + ((e_r + 1)/(2*e_r)) * (math.pi**2))                                    # 4
z_0 = (n_0/(2*math.pi*math.sqrt(2)*math.sqrt(e_r + 1))) * (math.log(1 + 4*(h/w_eff)*(x_1 + x_2)))                                         # 1

print(n_0/(2*math.pi*math.sqrt(2)*math.sqrt(e_r + 1)))
print(math.log(1 + 4*(h/w_eff)*(x_1 + x_2)))

print("w_eff =", w_eff)
print("x_1 =", x_1)
print("x_2 =", x_2)
print("z_0 =", z_0)

u = w/h                 # 5
g = s/h                 # 6

print("u =", u)
print("g =", g)

if u < 1:
    er_eff = ((e_r + 1)/2) + ((e_r - 1)/2)*(math.sqrt(w/(w+12*h)) + 0.04 * (1 - (w/h))**2)
else:
    er_eff = ((e_r + 1)/2) + ((e_r - 1)/2)*(math.sqrt(w/(w+12*h)))

print("er_eff =", er_eff)

a_0 = 0.7287*(er_eff - ((e_r + 1)/2)) * (math.sqrt(1-math.exp(-0.179*u)))
b_0 = (0.747*e_r)/(0.15+e_r)
c_0 = b_0 - (b_0 - 0.207) * math.exp(-0.414*u)
d_0 = 0.593 + 0.694 * math.exp(-0.562*u)
q_1 = 0.8695 * (u**0.194)
q_2 = 1 + 0.7519 * g + 0.189 * (g**2.31)
q_3 = 0.1975 + ((16.6+((8.4/g)**6))**(-0.387)) + (1/241)*(math.log((g**10)/(1+(g/3.4)**10)))
q_4 = (2*q_1)/(q_2*(math.exp(-g)*(u**q_3)+(2-math.exp(-g))*(u**(-q_3))))
q_5 = 1.794 + 1.14 * math.log(1 + (0.638/(g+0.517*(g**2.43))))
q_6 = 0.2305 + (1/281.3) * math.log((g**10)/(1+(g/5.8)**10)) + (1/5.1) * math.log(1+0.598*(g**1.154))
q_7 = (10+190*(g**2))/(1+82.3*(g**3))
q_8 = math.exp(-6.5-0.95*math.log(g)-((g/0.15)**5))
q_9 = math.log(q_7) * (q_8 + (1/16.5))
q_10 = (1/q_2) * (q_2*q_4-q_5*math.exp(math.log(u)*q_6*(u**(-q_9))))
er_eff0 = ((0.5*(e_r+1)+a_0-er_eff)*math.exp((-c_0)*(g**d_0))) + er_eff
z_diff = z_0*((math.sqrt(er_eff/er_eff0))/(1-((z_0/n_0)*q_10*math.sqrt(er_eff))))

print("a_0 =", a_0)
print("b_0 =", b_0)
print("c_0 =", c_0)
print("d_0 =", d_0)
print("q_1 =", q_1)
print("q_2 =", q_2)
print("q_3 =", q_3)
print("q_4 =", q_4)
print("q_5 =", q_5)
print("q_6 =", q_6)
print("q_7 =", q_7)
print("q_8 =", q_8)
print("q_9 =", q_9)
print("q_10 =", q_10)
print("er_eff0 =", er_eff0)
print("z_diff =", z_diff)
