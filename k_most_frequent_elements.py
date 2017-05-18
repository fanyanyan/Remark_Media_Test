# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:10:18 2017

@author: fanyanyan
"""


"""
时间复杂度分析：

每个函数的时间复杂度分析见函数定义后面的注释，总体的时间复杂度等于各个时间复杂度的总计加和。
T(n)=O((n-k)logk)+O(klogk)+...O(其他低阶复杂度）=O(nlogk)

所以本算法的时间复杂度T(n)=O(nlogk) is better than O(nlogn).

"""



def key_counter(array):           #时间复杂度O(n)
    '''
    对字典中的key进行计数
    Parameters
    ----------
    array: list (required)
        输入数组    
    '''
    hashdict={}
    for key in array:
        if not hashdict.keys().__contains__(key):
            hashdict[key]=1
        else:
            hashdict[key] = hashdict[key]+1
    # print(hashdict)
    return hashdict


def buildHeap(a):                # 外层循环时间复杂度(k)
    '''建立最小堆

    Parameters
    ----------
    a: list (required)
        代表键值对的二维数组
    size：int (required)
        数组的长度
    '''
    size=len(a)
    for j in range(int(size / 2) - 1, -1, -1):
        adjustHeap(a, j,size)
    return a


# 调整最小堆
def adjustHeap(a, i,size):       # 完全无顺序的数组建堆时间复杂度为  O(KlogK) 其中k=数组尺寸size。如果仅仅下沉最小堆顶点，时间复杂度为O(logk)
    '''调整堆，将左右孩子与根节点最小的放到根节点上。

    Parameters
    ----------
    a: list (required)
        代表键值对的二维数组
    i: int (required)
        从第几个非叶子节点开始调整堆
    size：int (required)
        数组的长度
    '''
    # size=len(a)
    lchild = 2 * i +1 # i的左孩子节点序号
    rchild = 2 * i + 2  # i的右孩子节点序号
    minIndex = i
    if i < size / 2:
        if lchild <= size-1 and a[lchild][1] < a[minIndex][1]:
            minIndex = lchild
        if rchild <= size-1 and a[rchild][1] < a[minIndex][1]:
            minIndex = rchild
        if minIndex != i:
            a[i], a[minIndex] = a[minIndex], a[i]
            adjustHeap(a, minIndex,size)


def get_2D_list_from_dict(myDict):      #时间复杂度为O(k),k为数组/字典长度。
    '''从字典中建立二维数组
    
    Parameters
    ----------
    myDict: dict (required)
        键值对字典
    '''
    list2D=[]
    for key in myDict.keys():
        list2D.append([key,myDict[key]])
    return list2D


def get_k_most_heap(list2d,k):         #时间复杂度为O((n-k)logK)。n为键值对的整个数组长度，k为前k个最大频率值。
    '''获取最大的k个元素的最小堆。

    Parameters
    ----------
    list2d: list[[]] (required)
        以二维数组形式存储的最小堆
    k: int(required)
        k个元素
    '''
    list2d_k=list2d[0:k]
    buildHeap(list2d_k)
    for otherElem in range(k,len(list2d)):
        # 如果剩下的元素的value大于堆顶的最小值，就代替堆顶值，并调整堆为最小堆。
        if list2d[otherElem][1]>list2d_k[0][1]:
            list2d_k[0]=list2d[otherElem]
            adjustHeap(list2d_k,0,k)
    return list2d_k


def heap_sort(list2d):                 #时间复杂度<O(KlogK)
    '''利用最小堆进行排序。

    Parameters
    ----------
    list2d: list[[]] (required)
        以二维数组形式存储的最小堆
    '''
    list2dInner=list2d
    size=len(list2dInner)
    # if size>=3:
    for end in range(size -1, -1, -1):
        if end >=0:
            list2dInner[0], list2dInner[end] = list2dInner[end], list2dInner[0]
            adjustHeap(list2dInner, 0, end - 1)
    if len(list2dInner)==3 and list2dInner[1][1]<list2dInner[2][1]:
        list2dInner[1][1],list2dInner[2][1]=list2dInner[2][1],list2dInner[1][1]
    if len(list2dInner)==2 and list2dInner[0][1]<list2dInner[1][1]:
        list2dInner[0][1],list2dInner[1][1]=list2dInner[1][1],list2dInner[0][1]

    return list2dInner


def get_k_most_keyValue_sortedByValue(array,k):     #总体的时间复杂度等于上面时间复杂度的加和。
    '''获取最大数组array中最大频率的前k个元素，
    
    Parameters
    ----------
    array: list (required)
        需要处理的数组
    k: int(required)
        最大的k个元素
    '''
    myDict = key_counter(array)                    #从数组中计算每个元素的出现次数，并返回键值对字典
    list2d = get_2D_list_from_dict(myDict)         #从键值对中获取键值对的二维数组表现形式
    kmost_heap = get_k_most_heap(list2d, k)        #获取k个最高频的最小堆数组。
    sortedHeap=heap_sort(kmost_heap)               #对已经获取的k_most_frequent最小堆排序。
    return sortedHeap


if __name__ == "__main__":
    rowlist=['q','w','w','s','s','s','e','e','c','z','z','z','z','z','a','a','a','a','g',]
    print('输入数组是：')
    print(rowlist)
    k=2
    print("前 "+str(k)+' 个最高频的键值对是：')
    print(get_k_most_keyValue_sortedByValue(rowlist,k))