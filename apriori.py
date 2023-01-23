import numpy as np

def load_data(data_path):
    """
    Load transactional data from a specified file path
    
    Parameters:
    data_path (string) : The file path of the data to be loaded
    
    Returns:
    Transactions (list) : A list of lists, where each sub-list represents a transaction and contains the items in that transaction
    """
    Transactions = []
    with open (data_path, 'r') as data:
        for lines in data:
            str_line = list(lines.strip().split(' '))
            Transactions.append(str_line)
    return Transactions

def find_uniItems(transactions):
    """
    Find unique items in the transactional data
    
    Parameters:
    transactions (list) : A list of lists, where each sub-list represents a transaction and contains the items in that transaction
    
    Returns:
    unique_items (list) : A list of unique items in the transactional data
    """
    unique_items = []
    for i in transactions:
        for j in i:
            if j not in unique_items:
                unique_items.append(j)
    return unique_items

def count_occourences(itemset, transactions):
    """
    Count the occurrences of an itemset in the transactional data
    
    Parameters:
    itemset (list) : A list of items representing the itemset to be counted
    transactions (list) : A list of lists, where each sub-list represents a transaction and contains the items in that transaction
    
    Returns:
    count (int) : The number of occurrences of the itemset in the transactional data
    """
    count = 0
    for i in range(len(transactions)):
        if set(itemset).issubset(set(transactions[i])):
            count = count + 1
    return count

def get_frequent(itemsets, Transactions, min_support, prev_discarded):
    """
    Get frequent itemsets and their support counts, and update the discarded itemsets
    
    Parameters:
    itemsets (list) : A list of itemsets to be checked for frequency
    Transactions (list) : A list of lists, where each sub-list represents a transaction and contains the items in that transaction
    min_support (float) : The minimum support threshold for determining frequent itemsets
    prev_discarded (dictionary) : A dictionary of itemsets that have previously been discarded
    
    Returns:
    L (list) : A list of frequent itemsets
    support_count (list) : A list of integers, where the nth element corresponds to the support count of the nth frequent itemset in the L list
    new_discarded (list) : A list of itemsets that do not meet the minimum support threshold and have been discarded
    """
    L = []
    support_count = []
    new_discarded = []
    num_transactions = len(Transactions)
    k = len(prev_discarded.keys())
    for s in range(len(itemsets)):
      discarded_before = False
      if k > 0:
        for it in prev_discarded[k]:
          if set(it).issubset(set(itemsets[s])):
            discarded_before = True
            break
      if not discarded_before:
        count = count_occourences(itemsets[s], Transactions)
        if count/num_transactions >= min_support:
          L.append(itemsets[s])
          support_count.append(count)
        else:
          new_discarded.append(itemsets[s])

    return L, support_count, new_discarded

def print_table(T, support_count):
    """
    Print the frequent itemsets and their support counts
    
    Parameters:
    T (list) : List of frequent itemsets
    support_count (list) : A list of integers, where the nth element corresponds to the support count of the nth frequent itemset in the T list
    
    Returns:
    None
    """
    print("Itemset  | Frequency")
    for k in range(len(T)):
        print("{}   :   {}".format(T[k],support_count[k]))
    print("\n\n")


def join_two_itemsets(item1, item2):
    """
    Join two itemsets
    
    Parameters:
    item1 (list) : First itemset to be joined
    item2 (list) : Second itemset to be joined
    
    Returns:
    item_out (list) : A new itemset that is the result of joining the two input itemsets
    """
    item1.sort()
    item2.sort()
    for i in range(len(item1)-1):
        if (item1[i]!=item2[i]):
            return []
    if item1[-1] != item2[-1]:
        item_out = item1 + [item2[-1]]
        return item_out
    else:
        return []

def join_itemsets(setofItemSets):
    """
    Join a set of itemsets
    
    Parameters:
    setofItemSets (list) : A list of itemsets to be joined
    
    Returns:
    C (list) : A new list of itemsets that are the result of joining the input itemsets
    """
    c = []
    for i in range(len(setofItemSets)):
        for j in range(i+1, len(setofItemSets)):
            item_out = join_two_itemsets(setofItemSets[i],setofItemSets[j])
            if len(item_out) > 0:
                c.append(item_out)
    return c

C = {}  #candidate item set
L = {}  #frequent item set

path = "/home/adarsh/Downloads/Semester 2/Data Mining/Assignment 1/retail_data.txt"
transactions = load_data(path)

unique_items = find_uniItems(transactions)
#print("Unique_items in the transactional data are:\n{}".format(unique_items))

itemset_size = 1
discarded = {itemset_size: []}
min_support = 0.4
C.update({itemset_size: [[f] for f in unique_items]})

# Get the first set of frequent itemsets and their support counts
support_count_L = {}
f, support, new_discarded = get_frequent(C[itemset_size], transactions, min_support, discarded)
discarded.update({ itemset_size : new_discarded})
L.update({itemset_size: f})
support_count_L.update({itemset_size: support})

# Print the first set of frequent itemsets and their support counts
print("L1:\n")
print_table(L[1], support_count_L[1])

# Iterate to find subsequent sets of frequent itemsets
k = itemset_size + 1
convergence = 0
while convergence == 0:
    C.update({k : join_itemsets(L[k-1])})
    f, support, new_discarded = get_frequent(C[k], transactions, min_support, discarded)
    discarded.update({k: new_discarded})
    support_count_L.update({k:support})
    L.update({k : f})
    if len(L[k])==0:
        convergence = True
    k+=1   
