'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Test Cases:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
'''

class Solution:
    def __init__(self):
        self.accountConnections = defaultdict(set)
        self.emailToName = {}
        self.seen = set()
    
    
    def buildConnections(self, accounts):
        for account in accounts:
            name = account[0]
            email1 = account[1]
            for i in range(1, len(account)):
                self.accountConnections[email1].add(account[i])
                self.accountConnections[account[i]].add(email1)
                self.emailToName[account[i]] = name

    def dfs(self, node):
        if node in self.seen:
            return []
        
        self.seen.add(node)
        connections = self.accountConnections[node]
        result = [node]

        for connection in connections:
            result += self.dfs(connection)
        return result

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.buildConnections(accounts)
        merged_accounts = []

        for account in self.accountConnections:
            merged = self.dfs(account)
            name = self.emailToName[account]

            if merged:
                merged.sort()
                merged_accounts.append([name] + merged)
        
        return merged_accounts
