#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
#import time
sys.setrecursionlimit(1000000000)

#gbl_call_quick_cnt = 0
#gbl_call_requick_cnt = 0
#gbl_i_loop_cnt = 0
#gbl_call_bubble_cnt = 0
#gbl_swap_cnt2 = 0
#gbl_line_count = 0
gbl_skip_inverse_left_cnt = 0
gbl_skip_inverse_right_cnt = 0

def bubble(a, start, end, sort_key):
    #global gbl_i_loop_cnt
    #global gbl_call_bubble_cnt
    
    #gbl_call_bubble_cnt += 1

    #swap_cnt = 0
    #i_loop_cnt = 0

    if start < end :
        for i in range ( start , end ) :
            #i_loop_cnt += 1
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

    #gbl_i_loop_cnt += i_loop_cnt
    #if sort_key == 3 :
    #    print( "DEBUG: i_loop_cnt = " , i_loop_cnt , "\t(" , gbl_i_loop_cnt , ")" )
    #if sort_key == 4 :
    #    #print( "DEBUG: point_3: i_loop_cnt = " , i_loop_cnt , "\t(" , gbl_i_loop_cnt , ")" )
    #    if gbl_i_loop_cnt % 1000 == 0 :
    #        print( "DEBUG: point_2: i_loop_cnt = " , i_loop_cnt , "\t(" , gbl_i_loop_cnt , ")" )

# end bubble sort function .

def quick(a, start, end):
    #global gbl_call_quick_cnt
    #gbl_call_quick_cnt+=1
    #swap_cnt=0

    if start < end: 
        left = start 
        pivot_pt = start + ( end - start ) // 2
        pivot_value = a[pivot_pt][3]
        # debug.
        #print("DEBUG: point-1: start, pivot, end = " , start , pivot_pt , end )
        for i in range(start, end+1): 
            #print("DEBUG: i = " , i , " .")
            if a[i][3] < pivot_value: 
                if i != left :
                    #swap_cnt+=1
                    a[i], a[left] = a[left], a[i] 
                if left == pivot_pt :
                    pivot_pt = i
                left += 1
                #if left > end :
                #    #print("ERROR: left is too big ( left: {} , end: {} ).".format(left,end))
                #    sys.stderr.write("ERROR: left is too big ( left: {} , end: {} ).\n".format(left,end))
                    
        # end for loop

        #print("DEBUG: point-2: start, pivot, end, i, left = " , start , pivot_pt , end , i , left )

        if a[left][3] > pivot_value :
            #swap_cnt+=1
            #if left >= pivot_pt :
            #    sys.stderr.write("ERROR: left -ge pivot_pt , ( {} , {} ).\n".format(left,pivot_pt))
            ##end debug print if
            a[left] , a[pivot_pt] = a[pivot_pt], a[left] 

        #if swap_cnt != 0 :
        #    quick(a, start, left-1)
        #    quick(a, left+1, end)
        # end if ( swap_cnt )
        
        quick(a, start, left-1)
        quick(a, left+1, end)

def quick21(a, start, end, sort_key):
    #global gbl_call_quick_cnt
    #gbl_call_quick_cnt+=1
    #swap_cnt=0
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

        # debug.
        #print("DEBUG: point-1: start, pivot, end = " , start , pivot_pt , end )
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
                
                #if left > end :
                #    #print("ERROR: left is too big ( left: {} , end: {} ).".format(left,end))
                #    sys.stderr.write("ERROR: left is too big ( left: {} , end: {} ).\n".format(left,end))
                    
        # end for loop

        #print("DEBUG: point-2: start, pivot, end, i, left = " , start , pivot_pt , end , i , left )

        if a[left][sort_key] > pivot_value :
            #swap_cnt+=1
            #if left >= pivot_pt :
            #    sys.stderr.write("ERROR: left -ge pivot_pt , ( {} , {} ).\n".format(left,pivot_pt))
            ##end debug print if
            a[left] , a[pivot_pt] = a[pivot_pt], a[left] 

        #if swap_cnt != 0 :
        #    quick(a, start, left-1)
        #    quick(a, left+1, end)
        # end if ( swap_cnt )
        
        #quick21(a, start, left-1, sort_key)
        #quick21(a, left+1, end, sort_key)

        #if left + 1 >= end :
        #    next
        #else :
        #    for l in range(left+1, end) :
        #        if a[l][sort_key] > a[l+1][sort_key] :
        #            inverse_count_right += 1
        #    # end for loop. (l)
        ## end if ( left + 1 > end )

        if inverse_count_left > 0 :
            quick21(a, start, left-1, sort_key)
        else :
            gbl_skip_inverse_left_cnt += 1

        #if inverse_count_right > 0 :
        #    quick21(a, left+1, end, sort_key)
        #else :
        #    gbl_skip_inverse_right_cnt += 1
        quick21(a, left+1, end, sort_key)

def requick(a, start, end):
    #global gbl_call_requick_cnt
    #gbl_call_requick_cnt += 1
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
    #global gbl_call_quick_cnt
    #global gbl_call_requick_cnt
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
            #line_count = line_count + 1
            #list_file.append(line)
            #str_file.append(list_file[coun].split()[3:4] + [line])
            #str_file.append([list_file[coun].split()[3],line])
            
            #str_file.append(line.split()[3:4] + [line])
            #str_file_order.append(line.split()[3:4] + [lines])
            #str_file_order.append(str_file[lines][0:1] + [lines])
            str_file.append(time_data + [line])
            str_file_order.append(time_data + [lines])
            coun=coun+1

        #quick(str_file, 0, len(str_file)-1)
        #quick21(str_file, 0, len(str_file)-1, 0)
        quick21(str_file_order, 0, len(str_file_order)-1, 0)
        #bubble(str_file, 0, len(str_file)-1)
        #bubble(str_file, 0, len(str_file)-1, 3)

        #print("DEBUG: gbl_call_quick_cnt = %d" , gbl_call_quick_cnt )

        for x in range(coun): 
            #in_file[fi].write(str(fi+1))
            #in_file[fi].write("  ")
            #for z in range(len(str_file[x])):
                #in_file[fi].write(str_file[x][z])
                #in_file[fi].write("  ")
            #in_file[fi].write("\n")
            #in_file_write_temp = str(fi+1) + "  " + "  ".join(str_file[x]) + "\n"
            #in_file[fi].write(in_file_write_temp)
            #in_file[fi].write(str(fi+1) + "  " + "  ".join(str_file[x]) + "\n")
            #in_file[fi].write(str(fi+1) + "  " + str_file[x][1])
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

    #for ne in range(fi_num):
    #    in_file[ne].close()

    print (q,"% 작성완료(파일).\n")

# end split function.

def combine():
    #global gbl_swap_cnt2
    #print ("2311345")
    q=(fi_num*line_num/10)
    p=0
    stop = 1

    str_file = []

    for ne in range(fi_num):
        op = 'sort_%d.txt'%(ne+1)
        #rein_file.append(open(op,'r',encoding='UTF-8'))
        #rein_file[ne].seek(0,0)
        in_file[ne].seek(0,0)
    
    reout_file = open('sort.txt','w',encoding='UTF-8')
    
    for fi in range(fi_num):
        list_file = []
        #str_file = []
        coun = 0
    
        #for lines in range(line_num):
        #    line = rein_file[fi].readline()
        #    list_file.append(line)
        #    str_file.append(list_file[coun].split())
        #    coun=coun+1
        #line = rein_file[fi].readline()
        line = in_file[fi].readline()
        #list_file.append(line)
        #str_file.append(list_file[0].split())
        #w_list.append(str_file[0])
        #str_file.append( [ list_file[0].split()[0] , list_file[0].split()[4] , "\t".join(list_file[0].split()[1:]) ] )
        str_file.append( [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ] )

    #requick(w_list, 0, len(w_list)-1)
    #bubble(w_list, 0, len(w_list)-1, 4)
    #bubble(str_file, 0, len(str_file)-1, 1)
    quick21(str_file, 0, len(str_file)-1, 1)

    #reinput_file = open('sort.txt','w',encoding='UTF-8')
    #for z in range(len(w_list[0])-1):
    #    reout_file.write(w_list[0][z+1])
    #    reout_file.write("   ")
    #reout_file.write("\n")

    #reout_file.close()

    #for ne in range(fi_num):
    #    in_file[ne].close()

    #for ne in range(fi_num):
    #    op = 'sort_%d.txt'%(ne+1)
    #    lain_file.append(open(op,'r',encoding='UTF-8'))
    #laout_file = open('sort.txt','a',encoding='UTF-8')
    
    fi=0
    
    while(1):
        fi=fi+1    
        relist_file = []
        restr_file = []
        comparison=[]
        coun = 0
        #fi_ch = w_list[0][0]
        fi_ch = str_file[0][0]
        #lain_file[int(fi_ch)-1].seek(0)
        
        #for z in range(len(w_list[0])-1):
        #    reout_file.write(w_list[0][z+1])
        #    reout_file.write("   ")
        #reout_file.write("\n")
        #reout_file.write("   ".join(w_list[0][1:]) + "\n")
        reout_file.write(str_file[0][2] + "\n")
        #time.sleep(1)

        stop=stop+1 

        #for lines in range(line_num):
        #    line = lain_file[int(fi_ch)-1].readline()
        #    relist_file.append(line)
        #    restr_file.append(relist_file[coun].split())
        #    comparison.append(relist_file[coun].split())
        #    coun=coun+1
        #next_line = comparison.index(w_list[0])
        #line = rein_file[int(fi_ch)-1].readline()
        line = in_file[int(fi_ch)-1].readline()
        #relist_file.append(line)
        #restr_file.append(relist_file[0].split())
        #comparison.append(relist_file[0].split())

        #print("DEBUG: w_list[0] = ", w_list[0])
        #del w_list[0]
        #try:
        #    #w_list.append(restr_file[(next_line+1)])
        #    #w_list.insert(0,restr_file[(next_line+1)])
        #    if line != "" :
        #        n = 0
        #        for n in range ( 0 , len(w_list)):
        #            if restr_file[0][4] > w_list[n][4]:
        #                if n == len(w_list) - 1 :
        #                    n += 1
        #                continue
        #            else :
        #                break
        #        gbl_swap_cnt2 += 1
        #        #w_list.insert(0,restr_file[0])
        #        w_list.insert(n,restr_file[0])
        #    else :
        #        next
        #        #continue
        #except:
        #    next
        
        # new del-insert logic.
        if line != "" :
            #w_list[0] = restr_file[0]
            #restr_file.append( [ relist_file[0].split()[0] , relist_file[0].split()[4] , "\t".join(relist_file[0].split()[1:]) ] )
            #str_file[0] = restr_file[0]
            #str_file[0] = [ relist_file[0].split()[0] , relist_file[0].split()[4] , "\t".join(relist_file[0].split()[1:]) ]
            str_file[0] = [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ]
        else :
            #del w_list[0]
            in_file[int(str_file[0][0])-1].close()
            del str_file[0]
        # end new del-insert logic.
        #requick(w_list, 0, len(w_list)-1)
        #bubble(w_list, 0, len(w_list)-1, 4)
        # find smallest element from array.
        #smallest_pt = 0
        #smallest_value = w_list[0][4]
        #for m in range(1 , len(w_list)):
        for m in range(0 , len(str_file)-1):
            if str_file[m][1] > str_file[m+1][1]:
                #gbl_swap_cnt2 += 1
                str_file[m] , str_file[m+1] = str_file[m+1] , str_file[m]
            else :
                # break for loop ( m ).
                # no need to go futher cause w_list is sorted.
                break
        # end for loop ( m ).
    
        # swap two elements in array(w_list).
        #print("DEBUG: smallest_pt = " , smallest_pt ) 
        #if smallest_pt != 0 :
        #    w_list[0] , w_list[smallest_pt] = w_list[smallest_pt] , w_list[0]
        # end if
    
        # end find .

        if(q==stop):
            q=q+(fi_num*line_num/10)
            p=p+10
            print(p,"%작성중(통합파일)")
            #print("DEBUG: gbl_swap_cnt2 = " , gbl_swap_cnt2 , end='')
            #reout_file.flush()
            #print(" .")
            

        if(stop==(fi_num*line_num)):
            #for z in range(len(str_file[0])-1):
            #    reout_file.write(str_file[0][z+1])
            #    reout_file.write("   ")
            reout_file.write(str_file[0][2] + "\n")
            print("통합 파일 작성완료")
            break
    
    print("INFO: closing infiles")
    #for ne in range(fi_num):
    #    #rein_file[ne].close()
    #    in_file[ne].close()
    in_file[int(str_file[0][0])-1].close()
    #reout_file.flush()
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

