#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(1000000000)


def quick(a, start, end):
    global call_quick_cnt
    call_quick_cnt+=1
    if start < end: 
        left = start 
        pivot = a[end][3]
        for i in range(start, end): 
            if a[i][3] < pivot: 
                a[i], a[left] = a[left], a[i] 
                left += 1 
        a[left] , a[end] = a[end], a[left] 
        quick(a, start, left-1)
        quick(a, left+1, end)

def requick(a, start, end):
    if start < end: 
        left = start 
        pivot = a[end][4]
        for i in range(start, end): 
            if a[i][4] < pivot: 
                a[i], a[left] = a[left], a[i] 
                left += 1 
        a[left] , a[end] = a[end], a[left] 
        requick(a, start, left-1)
        requick(a, left+1, end)

#원본 파일 분활 
def  split():
    p=0
    q=0
    origin_file = open('ol_cdump_2020-11-30.txt','r',encoding='UTF-8')

    for ne in range(fi_num):
        op = 'sort_%d.txt'%(ne+1)
        in_file.append(open(op,'w',encoding='UTF-8'))

    for fi in range(fi_num):
        list_file = []
        str_file = []
        coun = 0
    
        for lines in range(line_num):
            line = origin_file.readline()
            list_file.append(line)
            str_file.append(list_file[coun].split())
            coun=coun+1

        print("DEBUG: call_quick_cnt = " , call_quick_cnt)
        quick(str_file, 0, len(str_file)-1)

        for x in range(coun): 
            in_file[fi].write(str(fi+1))
            in_file[fi].write("  ")
            for z in range(len(str_file[x])):
                in_file[fi].write(str_file[x][z])
                in_file[fi].write("  ")
            in_file[fi].write("\n")
        if (fi==p):
            p=p+(fi_num/10)
            q=q+10
            print (q,"% 작성완료(파일)")

    origin_file.close

    for ne in range(fi_num):
        in_file[ne].close()

def combine():
    print ("2311345")
    q=(fi_num*line_num/10)
    p=0
    stop = 1

    for ne in range(fi_num):
        op = 'sort_%d.txt'%(ne+1)
        rein_file.append(open(op,'r',encoding='UTF-8'))
    
    reout_file = open('sort.txt','w',encoding='UTF-8')
    
    for fi in range(fi_num):
        list_file = []
        str_file = []
        coun = 0
    
        for lines in range(line_num):
            line = rein_file[fi].readline()
            list_file.append(line)
            str_file.append(list_file[coun].split())
            coun=coun+1
        w_list.append(str_file[0])

    requick(w_list, 0, len(w_list)-1)
        
    reinput_file = open('sort.txt','w',encoding='UTF-8')
    for z in range(len(w_list[0])-1):
        reinput_file.write(w_list[0][z+1])
        reinput_file.write("   ")
    reinput_file.write("\n")

    reout_file.close

    for ne in range(fi_num):
        in_file[ne].close()

    for ne in range(fi_num):
        op = 'sort_%d.txt'%(ne+1)
        lain_file.append(open(op,'r',encoding='UTF-8'))
    laout_file = open('sort.txt','a',encoding='UTF-8')
    
    fi=0
    
    while(1):
        fi=fi+1    
        relist_file = []
        restr_file = []
        comparison=[]
        coun = 0
        fi_ch = w_list[0][0]
        lain_file[int(fi_ch)-1].seek(0)
        
        for z in range(len(w_list[0])-1):
            laout_file.write(w_list[0][z+1])
            laout_file.write("   ")
        laout_file.write("\n")
        stop=stop+1 

        for lines in range(line_num):
            line = lain_file[int(fi_ch)-1].readline()
            relist_file.append(line)
            restr_file.append(relist_file[coun].split())
            comparison.append(relist_file[coun].split())
            coun=coun+1
        next_line = comparison.index(w_list[0])
        del w_list[0]
        try:
            w_list.append(restr_file[(next_line+1)])
        except:
            next

        requick(w_list, 0, len(w_list)-1)

        if(q==stop):
            q=q+(fi_num*line_num/10)
            p=p+10
            print(p,"%작성중(통합파일)")
            

        if(stop==(fi_num*line_num)):
            for z in range(len(w_list[0])-1):
                laout_file.write(w_list[0][z+1])
                laout_file.write("   ")
            print("통합 파일 작성완료")
            break
    
    for ne in range(fi_num):
        lain_file[ne].close()
    laout_file.close()
    
call_quick_cnt = 0
call_requick_cnt = 0
fi_num = 2000 #파일 갯수
line_num = 2000 # 나눌 줄수
in_file=[] #
rein_file=[]
lain_file=[]
w=[]       #
w_list=[]


split()
print("INFO: call_quick_cnt = " , call_quick_cnt)
print("INFO: call_requick_cnt = " , call_requick_cnt)

#combine()
print("INFO: call_quick_cnt = " , call_quick_cnt)
print("INFO: call_requick_cnt = " , call_requick_cnt)
