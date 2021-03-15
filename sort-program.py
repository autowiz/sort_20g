#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(1000000000)

#gbl_skip_inverse_left_cnt = 0
#gbl_skip_inverse_right_cnt = 0
#gbl_recursion_level = 0

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


def work_listed_quick(a, start, end, sort_key):
    #global gbl_skip_inverse_left_cnt
    #global gbl_skip_inverse_right_cnt

    work_list = []
    work_element = [start,end]
    #executed=0
    #work_element = [start,end,executed]
    # # # #work_list.insert( len(work_list) , work_element )
    while_loop_cnt = 0
    work_list_length_sum = 0
    work_list_length_max = 0
    slice_max = 4
    slice_point = []

    passed_start = start
    passed_end = end

    # make slice_point list ( each's start and end ) .
    current_slice_start = 0
    current_slice_end = 0
    current_slice_size = int ( ( end - start + 1 ) / slice_max )
    for i in range(slice_max) :
        current_slice_end = current_slice_start + current_slice_size
        if current_slice_end > end :
            current_slice_end = end
            current_slice_size = current_slice_end - current_slice_start

        slice_element = [current_slice_start , current_slice_end]
        slice_point.append(slice_element)
        work_list.append(slice_element)
        current_slice_start = current_slice_end + 1

    # check last slice's end point is equal to passed_end .
    if slice_point[-1][1] != passed_end :
        print("INFO: last slice's end is resetted with passed_end (" , slice_point[-1][1] , "->" , passed_end ,")")
        slice_point[-1][1] == passed_end


    # end for loop.

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
                #work_list.insert( len(work_list) , [start,left-1] )
                work_list.append( [start,left-1] )
                #work_list.insert( len(work_list) , [start,left-1,0] )
            #else :
            #    gbl_skip_inverse_left_cnt += 1
            
            #quick21(a, left+1, end, sort_key)
            #work_list.insert( len(work_list) , [left+1,end] )
            work_list.append( [left+1,end] )
            #work_list.insert( len(work_list) , [left+1,end,0] )
        # end if ( start < end ) .

    # end while loop

    # write to file.

    slice_fd = []
    for i in range ( slice_max ) :
        slice_element = slice_point[i]
        slice_fd.insert(i , open('slice_temp_'+str(i),'w+',encoding='UTF-8') )
        for j in range ( slice_point[i][0] , slice_point[i][1] + 1 ) :
            slice_fd[i].write( "\t".join(a[j]) )
        #slice_fd[i].flush()


    line = ""

    # read from files.
    merge_list = []
    for i in range ( slice_max ) :
        slice_fd[i].seek(0)
        line = slice_fd[i].readline()
        #merge_list[i] = [i] + line.split()[0:1] + line.split()[1:]
        if line != "" :
            date_data_len = len ( line.split()[0] )
            origin_line_data = line[date_data_len + 1 :]
            #merge_list.insert ( i , [i] + line.split()[0:1] + ["\t".join(line.split()[1:])] )
            merge_list.insert ( i , [i] + line.split()[0:1] + [origin_line_data] )

    short_bb_sort_cnt=0
    for i in range ( slice_max ) :
        #for j in range ( i , slice_max - 1 ) :
        short_bb_sort_cnt = 0
        for j in range ( slice_max - i - 1 ) :
            if merge_list[j][1] > merge_list[j+1][1] :
                short_bb_sort_cnt += 1
                merge_list[j] , merge_list[j+1] = merge_list[j+1] , merge_list[j]
        if short_bb_sort_cnt == 0 :
            break

    # merge .
    for i in range ( passed_start , passed_end + 1 ) :
        a[i] = merge_list[0][1:]
        current_slice_number = merge_list[0][0]
        line = slice_fd[current_slice_number].readline()
        if line != "" :
            date_data_len = len ( line.split()[0] )
            origin_line_data = line[date_data_len + 1 :]
            #merge_list[0] = [current_slice_number] + line.split()[0:1] + ["\t".join(line.split()[1:])]
            merge_list[0] = [current_slice_number] + line.split()[0:1] + [origin_line_data]
        else :
            slice_fd[current_slice_number].close()
            del merge_list[0]

        # small sort
        for j in range ( len ( merge_list ) - 1 ) :
            if merge_list[j][1] > merge_list[j+1][1] :
                merge_list[j] , merge_list[j+1] = merge_list[j+1] , merge_list[j]
            else :
                break
        # end small sort
    # end for loop.


    #print ( "DEBUG: work_list length2 = " , work_list_length_max , "\t" , work_list_length_sum , "\t" , while_loop_cnt ) 


#원본 파일 분활 
def  split():
    #global gbl_skip_inverse_left_cnt
    #global gbl_skip_inverse_right_cnt

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
        #str_file_order = []
        coun = 0

        for lines in range(line_num):
            line = origin_file.readline()
            time_data = line.split()[3:4]

            str_file.append(time_data + [line])
            #str_file_order.append(time_data + [lines])
            #str_file.append([str(fi+1)] + time_data + [line])
            #coun=coun+1

        #quick21(str_file_order, 0, len(str_file_order)-1, 0)
        #bubble(str_file_order, 0, len(str_file_order)-1, 0)
        #double_bubble(str_file_order, 0, len(str_file_order)-1, 0)
        #work_listed_quick(str_file_order, 0, len(str_file_order)-1, 0)
        work_listed_quick(str_file, 0, len(str_file)-1, 0)
        #work_listed_quick(str_file, 0, len(str_file)-1, 1)
        #quick21(str_file_order, 0, len(str_file_order)-1, 0)
        #temp_sorted = sorted(str_file_order, key=lambda x: x[0])
        #str_file_order = temp_sorted
        #str_file = sorted(str_file, key=lambda x: x[0])

        # write file using sorted list(array) .
        #for x in range(coun): 
        #    in_file[fi].write(str(fi+1) + "  " + str_file[int(str_file_order[x][1])][1])
            #in_file[fi].flush()
        #in_file[fi].flush()
        
        # write file with directly sorted list(array) .
        #for x in range(coun): 
        for x in range(len(str_file)) : 
            #in_file[fi].write(str(fi+1) + "  " + str_file[int(str_file_order[x][1])][1])
            in_file[fi].write(str(fi+1) + "  " + str_file[x][1])
            #if str_file[x][1][-1] != "\n" :
            #    in_file[fi].write("\n")
            ## end if. ( insert new line )
            in_file[fi].flush()

        # use writelines method .
        #in_file[fi].writelines(["\t".join(i) for i in str_file])
        #in_file[fi].flush()

        if (fi>=p):
            p=p+(fi_num/10)
            print (q,"% 작성완료(파일)")
            q=q+10
            #print("DEBUG: gbl_call_bubble_cnt = " , gbl_call_bubble_cnt )
            #print("DEBUG: gbl_skip_inverse_left_cnt = " , gbl_skip_inverse_left_cnt )
            #print("DEBUG: gbl_skip_inverse_right_cnt = " , gbl_skip_inverse_right_cnt )
    # end for loop ( fi ).

    origin_file.close()

    print (q,"% 작성완료(파일).\n")

# end split function.

def combine():
    q=(fi_num*line_num/10)
    p=0
    stop = 1

    #file_close_cnt = fi_num

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
        #str_file.append( [ line.split()[0] , line.split()[5] , "\t".join(line.split()[2:]) ] )

    quick21(str_file, 0, len(str_file)-1, 1)
    #work_listed_quick(str_file, 0, len(str_file)-1, 1)

    fi=0
    
    while(1):
        fi=fi+1    
        relist_file = []
        restr_file = []
        comparison=[]
        coun = 0
        fi_ch = str_file[0][0]
        
        reout_file.write(str_file[0][2] + "\n")
        reout_file.flush()

        stop=stop+1 

        line = in_file[int(fi_ch)-1].readline()
        #try:
        #    line = in_file[int(fi_ch)-1].readline()
        #except:
        #    print("DEBUG: exception fi_ch = ", fi_ch , ".")

        loop_1 = 0
        temp_element = []
        bi_search_start = 0
        bi_search_end = 0
        bi_search_mid = 0

        # new del-insert logic.
        if line != "" :
            str_file[0] = [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ]
            #str_file[0] = [ line.split()[0] , line.split()[5] , "\t".join(line.split()[2:]) ]
            #temp_element = [ line.split()[0] , line.split()[4] , "\t".join(line.split()[1:]) ]
        else :
            in_file[int(str_file[0][0])-1].close()
            #file_close_cnt -= 1
            #print("DEBUG: file_close_cnt = " , file_close_cnt )
            #if file_close_cnt <= 0 :
            #    break
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
        #temp_element = str_file[0]
        #del str_file[0]
        bi_search_start = 1
        #bi_search_start = 0
        bi_search_end = len(str_file) - 1
        if bi_search_end < 0 :
            loop_1 = 0
            bi_search_end = 0
        bi_search_mid = bi_search_start + ( bi_search_end - bi_search_start ) // 2
        if len(str_file) > 1 and str_file[0][1] <= str_file[1][1] :
            ##combine_compare_cnt += 1
            loop_1 = 0
            bi_search_mid = 0
        # end if.

        while loop_1 == 1 :
            if bi_search_end < bi_search_start :
                break
            if bi_search_end == bi_search_start :
                #if str_file[bi_search_end][1] < temp_element[1] :
                if str_file[bi_search_end][1] < str_file[0][1] :
                    if bi_search_end != bi_search_mid :
                        print ( "ERROR: bi_search_end and bi_search_mid is not equal when start and end is equal.!!!" )
                    bi_search_mid = bi_search_end + 1
                break
            ##combine_compare_cnt += 1
            #if str_file[bi_search_mid][1] > temp_element[1] :
            if str_file[bi_search_mid][1] > str_file[0][1] :
                bi_search_end = bi_search_mid
            else :
                bi_search_start = bi_search_mid + 1
            bi_search_mid = bi_search_start + ( bi_search_end - bi_search_start ) // 2
        # end while loop ( loop_1 ).
        #temp_element = str_file[0]
        #del str_file[0]

        if bi_search_mid > 1 :
            #str_file.insert(bi_search_mid,temp_element) 
            str_file.insert(bi_search_mid,str_file[0]) 
            del str_file[0]

        if(q<=stop):
            q=q+(fi_num*line_num/10)
            p=p+10
            print(p,"%작성중(통합파일)")
            ##print("INFO: combine_compare_cnt = " , combine_compare_cnt)
        
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
fi_num = 2000 #파일 갯수
#fi_num = 20 #파일 갯수
#line_num = 20000 # 나눌 줄수
line_num = 2000 # 나눌 줄수
line_num = 200 # 나눌 줄수
in_file=[] #
rein_file=[]
lain_file=[]
w=[]       #
w_list=[]


split()

combine()

