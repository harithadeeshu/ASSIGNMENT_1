sum_of_no=(3,2,1,3,5,6)
n=(9,8,6,2,6,7,4,6,8)
def find_pairs(arr, n, sum_of_no):
    n = len(arr)
    sum_of_no = 6
    pairs_count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == sum_of_no:
                pairs_count += 1
    print("Pairs count = ", pairs_count)
arr = [0, 2, 1, 4, 5 ,7 ,-2, 8, 4]
find_pairs(arr,n,sum_of_no)