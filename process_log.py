f1=open('log_report.txt','w')
f2=open('log_report.csv','w')
f1.write('IP\tDATE\tPICS\tURL')
f2.writelines(['IP,','DATE,','PICS,','URL\n'])
f3=open(r'C:\Users\lab365\Desktop\PythonTraining\log\serverlog.txt')

for line in f3:
    if line[:3].isdigit():
        sp=line.split()
        #print(sp)
        ip=sp[0]
        #print(ip)
        dt=sp[3]
        dt1=dt[1:12]
        dt2=dt[1:dt.index(':')]
        # print(ip,dt2)
        if 'pics' in sp[6]:
            im=sp[6]
            im1=im[6:]
            im2=im.split('/')
            im2=im2[-1]
            im3=im.lstrip('/pics/')
            im4=im.replace('/pics/','')
        else:
            im1='No Image'
        url=sp[10][1:-1]
        print(ip,dt2,im1,url)
        print(ip,dt2,im1,url,sep='\t',file=f1)
        print(ip,dt2,im1,url,sep=',',file=f2)
f1.close()
f2.close()
f3.close()


