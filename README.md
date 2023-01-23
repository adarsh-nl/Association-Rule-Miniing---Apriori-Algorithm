# Association-Rule-Miniing---Apriori-Algorithm

This code is an implementation of the Apriori algorithm, which is a frequent itemset mining algorithm used in market basket analysis. The code includes functions that load transactional data from a file, find unique items in the data, count the occurrences of an itemset in the data, get frequent itemsets and their support counts, and print the frequent itemsets and their support counts. The Apriori algorithm works by iteratively generating new candidate itemsets from the frequent itemsets of the previous iteration, and then discarding any itemsets that do not meet the minimum support threshold. The final output is a list of frequent itemsets and their support counts.

The code has several functions that perform different tasks in the Apriori algorithm:

# load_data(data_path): 
This function takes a file path as input and loads transactional data from that file, returning the data as a list of lists where each sub-list represents a transaction and contains the items in that transaction.

# find_uniItems(transactions): 
This function takes a list of transactions as input and returns a list of unique items in the transactional data.

# count_occourences(itemset, transactions): 
This function takes an itemset and a list of transactions as input, and returns the number of occurrences of the itemset in the transactional data.

# get_frequent(itemsets, Transactions, min_support, prev_discarded): 
This function takes a list of itemsets, a list of transactions, a minimum support threshold, and a dictionary of itemsets that have previously been discarded as input, and returns a list of frequent itemsets, a list of integers representing the support count of each frequent itemset, and a list of itemsets that do not meet the minimum support threshold and have been discarded.

# print_table(T, support_count): 
This function takes a list of frequent itemsets and a list of integers representing the support count of each frequent itemset as input, and prints the frequent itemsets and their support counts in a tabular format.

# join_two_itemsets(item1, item2): 
This function takes two itemsets as input and returns a new itemset that is the union of the two input itemsets.

Note:
Description generated using ChatGPT
