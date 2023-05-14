"""
1169. Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""

from typing import List

class Solution:
    
    """
    We need to create a helper function to
    compare the two conditions using current transaction
    with the previous transaction.
    """
    
    def is_invalid(self, current_transaction, previous_transactions):
        cur_name, cur_time, cur_amount, cur_city = current_transaction.split(",")
        
        if int(cur_amount) > 1000:
            return True
        
        for prev_transaction in previous_transactions:
            prev_name, prev_time, _, prev_city = prev_transaction.split(",")
            
            if prev_name == cur_name and prev_city != cur_city and abs(int(cur_time) - int(prev_time)):
                return True
            
        return False
    
    def invalid_transactions(self, transactions: List[str]):
        
        invalid = []
        processed = []
        
        for transaction in transactions:
            if self.is_invalid(transaction, transactions):
                invalid.append(transaction)
                
            else:
                processed.append(transaction)
                
        return invalid
        