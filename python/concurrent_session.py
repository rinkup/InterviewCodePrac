def has_overlap(A_start, A_end,sessions):
    for B_sess in sessions:
        B_start, B_end =B_sess[0],B_sess[1]
        latest_start = max(A_start, B_start)
        earliest_end = min(A_end, B_end)
        if latest_start <= earliest_end:
            # print(A_start,A_end,B_start,B_end)
            return True
    else: 
        return False

session_list = [ [2,5], [3,6], [8,10],[9,10],[10,12], [9,20] ]
count=0
for i ,sess in enumerate(session_list):
    if has_overlap(sess[0],sess[1],session_list[i+1:]):
        count+=1
print(count)

