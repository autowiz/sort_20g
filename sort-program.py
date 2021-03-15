#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
#sys.setrecursionlimit(1000000000)

gbl_skip_inverse_left_cnt = 0
gbl_skip_inverse_right_cnt = 0
gbl_recursion_level = 0

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
        second_largest_value = None
        second_largest_pt = 0

        smallest_swap_cnt = 0
        largest_swap_cnt = 0
        second_largest_swap_cnt = 0
        compare_swap_cnt = 0

        element_temp=[]

        while local_len > 0 :
            inverse_cnt = 0

            smallest_pt=local_start
            largest_pt=local_end
            second_largest_pt=local_end
            smallest_value = a[local_start][sort_key]
            largest_value = a[local_end][sort_key]
            second_largest_value = a[local_end][sort_key]
            
            # search smallest and largest value . 
            # and check list is already sorted.

            #
            # search STEP 1.
            #
            i = local_start
            if a[i][sort_key] > a[i+1][sort_key] :
                a[i] , a[i+1] = a[i+1] , a[i]
                if a[i][sort_key] < smallest_value :
                    smallest_value = a[i][sort_key]
                    smallest_pt = i
                    compare_swap_cnt += 1
            #else :
            #    if a[i][sort_key] > largest_value :
            #        largest_value = a[i][sort_key]
            #        largest_pt = i
            # end if .
            last_value = a[i][sort_key]
            second_largest_value = a[i][sort_key]
            second_largest_pt = i
            # end firstt element compare.

            #
            # search STEP 2.
            #
            for i in range ( local_start+1 , local_end ) :
                #if a[i][sort_key] > a[i+1][sort_key] :
                #    a[i] , a[i+1] = a[i+1] , a[i]
                if a[i][sort_key] > a[i+1][sort_key] :
                    a[i] , a[i+1] = a[i+1] , a[i]
                    if a[i][sort_key] < smallest_value :
                        smallest_value = a[i][sort_key]
                        smallest_pt = i
                        compare_swap_cnt += 1
                    #if a[i+1][sort_key] > largest_value :
                    #    largest_value = a[i+1][sort_key]
                    #    largest_pt = i+1

                if last_value > a[i][sort_key] :
                    inverse_cnt += 1

                    # compare with second_largest_value.
                    if second_largest_value < last_value :
                        second_largest_value = last_value
                        second_largest_pt = i-1
                    # end if.
                # end if .

                last_value = a[i][sort_key]

                #if a[i][sort_key] < smallest_value :
                #    smallest_value = a[i][sort_key]
                #    smallest_pt = i
                #
                #if a[i][sort_key] > largest_value :
                #    largest_value = a[i][sort_key]
                #    largest_pt = i
            # end for ( i ).

            #
            # search STEP 3.
            #
            i = local_end
            #if last_value > a[i][sort_key] :
            #    print ("DEBUG: abnormal status 1")
            #    inverse_cnt += 1
            #last_value = a[i][sort_key]
            
            #if a[i][sort_key] < smallest_value :
            #    print ("DEBUG: abnormal status 2")
            #    smallest_value = a[i][sort_key]
            #    smallest_pt = i

            # skip below block cause, biggest element already moved to right(bottom) end.
            #if a[i][sort_key] > largest_value :
            #    largest_value = a[i][sort_key]
            #    largest_pt = i

            if a[i-1][sort_key] > second_largest_value :
                second_largest_value = a[i-1][sort_key]
                second_largest_pt = i-1
            # end if.

            #
            # search STEP Done.
            #

            # list is sorted then break while loop.
            if inverse_cnt == 0 :
                # break while loop (local_lne).
                break

            # swap smallest element to left .
            # swap largest element to right .
            #a[local_start] , a[smallest_pt] = a[smallest_pt] , a[local_start]
            #a[local_end] , a[largest_pt] = a[largest_pt] , a[local_end]
            if smallest_pt != local_start :
                element_temp = a[smallest_pt]
                del a[smallest_pt]
                a.insert(local_start,element_temp)
                smallest_swap_cnt += 1
            # must check if largest_pt is smaller than smallest_pt.
            #if largest_pt < smallest_pt :
            #    largest_pt += 1
            #element_temp = a[largest_pt]
            #del a[largest_pt]
            #a.insert(local_end,element_temp)

            # add second_largest_value search and swap logic.
            if second_largest_pt < smallest_pt :
                second_largest_pt += 1
            if second_largest_pt != local_end - 1 :
                element_temp = a[second_largest_pt]
                del a[second_largest_pt]
                a.insert(local_end-1,element_temp)
                second_largest_swap_cnt += 1
            # end add second_largest_value search and swap logic.

            local_start += 1
            local_end -= 1
            local_len = local_end - local_start
        # end while loop (local_len).

        print ( "INFO: double_bubble swap cnt = {}\t{}\t{} .".format(smallest_swap_cnt , second_largest_swap_cnt , compare_swap_cnt ) )

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

def work_listed_quick(a, start, end, sort_key):
    global gbl_skip_inverse_left_cnt
    global gbl_skip_inverse_right_cnt

    work_list = []
    work_element = [start,end]
    #executed=0
    #work_element = [start,end,executed]
    work_list.insert( len(work_list) , work_element )
    while_loop_cnt = 0
    work_list_length_sum = 0
    work_list_length_max = 0

    while len ( work_list ) > 0 :
        
        #while_loop_cnt += 1
        #work_list_length = len(work_list)
        #work_list_length_sum += work_list_length
        #if work_list_length > work_list_length_max :
        #    work_list_length_max = work_list_length

        #print ( "DEBUG: work_list length = " , len(work_list) , "\t" , while_loop_cnt ) 
        work_element = work_list.pop()
        #work_element = work_list[work_list_length-1]
        #if work_element[2] == 0 :
        #    # if executed value is 0 , then set value to 1
        #    work_list[work_list_length - 1][2] = 1
        #else :
        #    # if executed value is 1 , then delete element and do next
        #    del work_list[work_list_length -1]
        #    continue

        start = work_element[0]
        end = work_element[1]

        if start < end : 
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
    
            # for simple compare test ( left first and right first ) .
            #work_list.insert( len(work_list) , [left+1,end] )
            #work_list.insert( len(work_list) , [left+1,end,0] )

            if inverse_count_left > 0 :
                #quick21(a, start, left-1, sort_key)
                work_list.insert( len(work_list) , [start,left-1] )
                #work_list.insert( len(work_list) , [start,left-1,0] )
            #else :
            #    gbl_skip_inverse_left_cnt += 1
    
            #quick21(a, left+1, end, sort_key)
            work_list.insert( len(work_list) , [left+1,end] )
            #work_list.insert( len(work_list) , [left+1,end,0] )
        # end if ( start < end ) .

    # end while loop

    #print ( "DEBUG: work_list length2 = " , work_list_length_max , "\t" , work_list_length_sum , "\t" , while_loop_cnt ) 

def quick21(a, start, end, sort_key):
    global gbl_skip_inverse_left_cnt
    global gbl_skip_inverse_right_cnt
    #global gbl_recursion_level 

    #gbl_recursion_level += 1
    #print ( "DEBUG: recursion_level = " , gbl_recursion_level )

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

        quick21(a, left+1, end, sort_key)

        if inverse_count_left > 0 :
            quick21(a, start, left-1, sort_key)
        #else :
        #    gbl_skip_inverse_left_cnt += 1

        #quick21(a, left+1, end, sort_key)

    #gbl_recursion_level -= 1

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
        #double_bubble(str_file_order, 0, len(str_file_order)-1, 0)
        work_listed_quick(str_file_order, 0, len(str_file_order)-1, 0)
        #quick21(str_file_order, 0, len(str_file_order)-1, 0)
        #temp_sorted = sorted(str_file_order, key=lambda x: x[0])
        #str_file_order = temp_sorted

        for x in range(coun): 
            in_file[fi].write(str(fi+1) + "  " + str_file[int(str_file_order[x][1])][1])
        #in_file[fi].flush()

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
    combine_compare_cnt = 0

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

        try:
            line = in_file[int(fi_ch)-1].readline()
        except:
            print("DEBUG: exception fi_ch = ", fi_ch , ".")

        loop_1 = 0
        temp_element = []
        bi_search_start = 0
        bi_search_end = 0
        bi_search_mid = 0

        # new del-insert logic.
        if line != "" :
            str_file[0] = [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ]
            #temp_element = [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ]
        else :
            in_file[int(str_file[0][0])-1].close()
            del str_file[0]
            #temp_element = str_file[0]
        # end new del-insert logic.

        #for m in range(0 , len(str_file)-1):
        #    if str_file[m][1] > str_file[m+1][1]:
        #        #gbl_swap_cnt2 += 1
        #        str_file[m] , str_file[m+1] = str_file[m+1] , str_file[m]
        #        combine_compare_cnt += 1
        #    else :
        #        # break for loop ( m ).
        #        # no need to go futher cause str_file is sorted.
        #        break
        ## end for loop ( m ).

        loop_1 = 1
        temp_element = str_file[0]
        #del str_file[0]
        bi_search_start = 1
        #bi_search_start = 0
        bi_search_end = len(str_file) - 1
        if bi_search_end < 0 :
            loop_1 = 0
            bi_search_end = 0
        bi_search_mid = bi_search_start + ( bi_search_end - bi_search_start ) // 2
        if len(str_file) > 1 and str_file[0][1] <= str_file[1][1] :
            combine_compare_cnt += 1
            loop_1 = 0
            bi_search_mid = 0
        # end if.
        while loop_1 == 1 :
            if bi_search_end < bi_search_start :
                break
            if bi_search_end == bi_search_start :
                if str_file[bi_search_end][1] < temp_element[1] :
                    if bi_search_end != bi_search_mid :
                        print ( "ERROR: bi_search_end and bi_search_mid is not equal when start and end is equal.!!!" )
                    bi_search_mid = bi_search_end + 1
                break
            combine_compare_cnt += 1
            #if str_file[bi_search_mid][1] > str_file[0][1] :
            if str_file[bi_search_mid][1] > temp_element[1] :
                bi_search_end = bi_search_mid
            else :
                bi_search_start = bi_search_mid + 1
            bi_search_mid = bi_search_start + ( bi_search_end - bi_search_start ) // 2
        # end while loop ( loop_1 ).
        #temp_element = str_file[0]
        #del str_file[0]

        if bi_search_mid > 1 :
            str_file.insert(bi_search_mid,temp_element) 
            del str_file[0]

        if(q==stop):
            q=q+(fi_num*line_num/10)
            p=p+10
            print(p,"%작성중(통합파일)")
            print("INFO: combine_compare_cnt = " , combine_compare_cnt)

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

