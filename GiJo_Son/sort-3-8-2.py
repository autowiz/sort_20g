#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(1000000000)

gbl_skip_inverse_left_cnt = 0
gbl_skip_inverse_right_cnt = 0

def double_bubble(a, start, end, sort_key):
    if start < end :
        local_start = start
        local_end = end
        local_len = end - start
        last_value = None
        inverse_cnt = 0
        smallest_value = None
        smallest_pt = 0
        largest_value = None
        largest_pt = 0
        element_temp=[]

        while local_len > 0 :
            inverse_cnt = 0

            smallest_pt=local_start
            largest_pt=local_end
            smallest_value = a[local_start][sort_key]
            largest_value = a[local_end][sort_key]
            
            # search smallest and largest value . 
            # and check list is already sorted.
            for i in range ( local_start , local_end + 1 ) :
                if i < local_end :
                    if a[i][sort_key] > a[i+1][sort_key] :
                        a[i] , a[i+1] = a[i+1] , a[i]
                if i > local_start :
                    if last_value > a[i][sort_key] :
                        inverse_cnt += 1
                last_value = a[i][sort_key]

                if a[i][sort_key] < smallest_value :
                    smallest_value = a[i][sort_key]
                    smallest_pt = i

                if a[i][sort_key] > largest_value :
                    largest_value = a[i][sort_key]
                    largest_pt = i
            # end for ( i ).

            # list is sorted then break while loop.
            if inverse_cnt == 0 :
                # break while loop (local_lne).
                break

            # swap smallest element to left .
            # swap largest element to right .
            #a[local_start] , a[smallest_pt] = a[smallest_pt] , a[local_start]
            #a[local_end] , a[largest_pt] = a[largest_pt] , a[local_end]
            element_temp = a[smallest_pt]
            del a[smallest_pt]
            a.insert(local_start,element_temp)
            # must check if largest_pt is smaller than smallest_pt.
            if largest_pt < smallest_pt :
                largest_pt += 1
            element_temp = a[largest_pt]
            del a[largest_pt]
            a.insert(local_end,element_temp)

            local_start += 1
            local_end -= 1
            local_len = local_end - local_start
        # end while loop (local_len).

    # end if start < end
# end double_bubble sort function .

def bubble(a, start, end, sort_key):
    if start < end :
        for i in range ( start , end ) :
            swap_cnt = 0
            for j in range ( start , end ) :
                if a[j][sort_key] > a[j+1][sort_key] :
                    swap_cnt += 1
                    a[j] , a[j+1] = a[j+1] , a[j]
                # end if.
            # end for loop ( j )

            if swap_cnt == 0 :
                # break for loop (i)
                break
            # end if 
        # end for loop ( i )
    # end if start < end
# end bubble sort function .

def quick(a, start, end):
    if start < end: 
        left = start 
        pivot_pt = start + ( end - start ) // 2
        pivot_value = a[pivot_pt][3]
        for i in range(start, end+1): 
            #print("DEBUG: i = " , i , " .")
            if a[i][3] < pivot_value: 
                if i != left :
                    #swap_cnt+=1
                    a[i], a[left] = a[left], a[i] 
                if left == pivot_pt :
                    pivot_pt = i
                left += 1
        # end for loop

        if a[left][3] > pivot_value :
            a[left] , a[pivot_pt] = a[pivot_pt], a[left] 

        quick(a, start, left-1)
        quick(a, left+1, end)

def quick21(a, start, end, sort_key):
    global gbl_skip_inverse_left_cnt
    global gbl_skip_inverse_right_cnt

    if start < end: 
        left = start 
        pivot_pt = start + ( end - start ) // 2
        pivot_value = a[pivot_pt][sort_key]
        last_value_left = None
        last_value_right = None
        inverse_count_left = 0
        inverse_count_right = 0

        for i in range(start, end+1): 
            #print("DEBUG: i = " , i , " .")
            if a[i][sort_key] < pivot_value: 
                if i != left :
                    #swap_cnt+=1
                    a[i], a[left] = a[left], a[i] 
                if left == pivot_pt :
                    pivot_pt = i

                # new performance logic.
                if left > start :
                    if last_value_left > a[left][sort_key] :
                        inverse_count_left += 1
                last_value_left = a[left][sort_key]

                left += 1
                
        # end for loop

        if a[left][sort_key] > pivot_value :
            a[left] , a[pivot_pt] = a[pivot_pt], a[left] 

        if inverse_count_left > 0 :
            quick21(a, start, left-1, sort_key)
        #else :
        #    gbl_skip_inverse_left_cnt += 1

        quick21(a, left+1, end, sort_key)

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
    global gbl_skip_inverse_left_cnt
    global gbl_skip_inverse_right_cnt

    p=0
    q=0

    origin_file = open('ol_cdump_2020-11-30.txt','r',encoding='UTF-8')
    #origin_file = open('4m_lines_part_sorted.txt','r',encoding='UTF-8')

    for ne in range(fi_num):
        op = 'sort_%d.txt'%(ne+1)
        in_file.append(open(op,'w+',encoding='UTF-8'))

    for fi in range(fi_num):
        list_file = []
        str_file = []
        str_file_order = []
        coun = 0
    
        for lines in range(line_num):
            line = origin_file.readline()
            time_data = line.split()[3:4]

            str_file.append(time_data + [line])
            str_file_order.append(time_data + [lines])
            coun=coun+1

        #quick21(str_file_order, 0, len(str_file_order)-1, 0)
        #bubble(str_file_order, 0, len(str_file_order)-1, 0)
        double_bubble(str_file_order, 0, len(str_file_order)-1, 0)

        for x in range(coun): 
            in_file[fi].write(str(fi+1) + "  " + str_file[int(str_file_order[x][1])][1])
        if (fi==p):
            p=p+(fi_num/10)
            print (q,"% 작성완료(파일)")
            q=q+10
            #print("DEBUG: gbl_call_bubble_cnt = " , gbl_call_bubble_cnt )
            print("DEBUG: gbl_skip_inverse_left_cnt = " , gbl_skip_inverse_left_cnt )
            print("DEBUG: gbl_skip_inverse_right_cnt = " , gbl_skip_inverse_right_cnt )
    # end for loop ( fi ).

    origin_file.close()

    print (q,"% 작성완료(파일).\n")

# end split function.

def combine():
    q=(fi_num*line_num/10)
    p=0
    stop = 1

    str_file = []

    for ne in range(fi_num):
        op = 'sort_%d.txt'%(ne+1)
        in_file[ne].seek(0,0)
    
    reout_file = open('sort.txt','w',encoding='UTF-8')
    
    for fi in range(fi_num):
        list_file = []
        #str_file = []
        coun = 0
    
        line = in_file[fi].readline()
        str_file.append( [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ] )

    quick21(str_file, 0, len(str_file)-1, 1)

    fi=0
    
    while(1):
        fi=fi+1    
        relist_file = []
        restr_file = []
        comparison=[]
        coun = 0
        fi_ch = str_file[0][0]
        
        reout_file.write(str_file[0][2] + "\n")

        stop=stop+1 

        line = in_file[int(fi_ch)-1].readline()
        
        # new del-insert logic.
        if line != "" :
            str_file[0] = [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ]
        else :
            in_file[int(str_file[0][0])-1].close()
            del str_file[0]
        # end new del-insert logic.

        for m in range(0 , len(str_file)-1):
            if str_file[m][1] > str_file[m+1][1]:
                #gbl_swap_cnt2 += 1
                str_file[m] , str_file[m+1] = str_file[m+1] , str_file[m]
            else :
                # break for loop ( m ).
                # no need to go futher cause str_file is sorted.
                break
        # end for loop ( m ).
    
        if(q==stop):
            q=q+(fi_num*line_num/10)
            p=p+10
            print(p,"%작성중(통합파일)")

        if(stop==(fi_num*line_num)):
            reout_file.write(str_file[0][2] + "\n")
            print("통합 파일 작성완료")
            break
    
    print("INFO: closing infiles")
    in_file[int(str_file[0][0])-1].close()
    print("INFO: closing outfile")
    reout_file.close()
    
    print("INFO: outfile closed")

# end combine function.

#fi_num = 2000 #파일 갯수
fi_num = 200 #파일 갯수
#fi_num = 20 #파일 갯수
#line_num = 20000 # 나눌 줄수
line_num = 2000 # 나눌 줄수
in_file=[] #
rein_file=[]
lain_file=[]
w=[]       #
w_list=[]


split()

combine()

