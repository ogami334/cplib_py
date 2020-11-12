#ソース　https://juppy.hatenablog.com/entry/2018/11/17/蟻本_python_Binary_Indexed_Tree_競技プログラミング
#A1 ... AnのBIT(1-indexed)
BIT = [0]*(n+1)
#idxの一番下のbit
#A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum

#Ai += x O(logN)
def BIT_update(idx,x):
    while idx <= n:
        BIT[idx] += x
        idx += idx&(-idx)
    return
