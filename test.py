from sample import *

samp = Sample()

def neigh_test(n, R):
    s = S1()
    r = pi * R / n
    for i in range(n):
        random_loc = samp.u_samp(s)
        d = random_loc[0]
        coin = rand()
        # print "prob: " + str((r / float(d)))
        # print "coin: " + str(coin)
        if coin < (r / float(d)):
            s.insert_member(i, random_loc)
    return len(s.members_in_range(0,2 * pi))

n = 1000
R = 100
t = 2000
S = 0
for i in range(t):
    S += neigh_test(n, R)
print S/float(t)

print R * math.log(n/float(R))
