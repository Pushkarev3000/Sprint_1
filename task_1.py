time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_p = time.split(",")
time_p_2 =[]
time_p_3 =[]
time_p_4 =[]
time_p_5 =[]
time_p_6 =[]
time_sum_s = 0
time_sum_m = 0
a=1
b=1
for i in time_p:
    i = i.split()
    time_p_2.append(i)
for sublist in time_p_2:
    for item in sublist:
        time_p_3.append(item.replace("h", " 3600"))
for item in time_p_3:
    time_p_4.append(item.replace("m", " 60"))
for item in time_p_4:
    time_p_5.append(item.replace("s", " 1"))
for time_split in time_p_5:
    time_p_6.append(time_split.split())
for circle in time_p_6:
    a = 0
    b = 1
    for elem in circle:
        if elem == ''.join(circle[:1:1]):
            a = int(elem)
        if elem == ''.join(circle[1::1]):
            b = int(elem) * a
            time_sum_s = time_sum_s+b
time_sum_m = time_sum_s//60
time_sum_ost = time_sum_s%60
print('Общее время: '+str(time_sum_m)+'m '+str(time_sum_ost)+'s' )