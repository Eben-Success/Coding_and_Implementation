# Find most similar websites

"""
You are given a list of (website, user) pairs that represent user visiting websites.
Come up with a program that identifies the top k pairs of websites with the greatest
similarity.

For example, suppose k = 1, and the list of tuples is: 
[('google.com', 1), ('google.com', 3), ('google.com', 5), 
('pets.com', 1), ('pets.com', 2), ('yahoo.com', 6), 
('yahoo.com', 2), ('yahoo.com', 3), ('yahoo.com', 4), ('yahoo.com', 5) 
('wikipedia.org', 4), ('wikipedia.org', 5), ('wikipedia.org', 6), 
('wikipedia.org', 7), ('bing.com', 1), ('bing.com', 3), ('bing.com': 5), 
('bing.com', 6)] 

To compute the similarity between two websites you should compute the numbe of users
they have in common divided by the number of users who have visited either site in total.
This is known as Jaccard index.

For example, in this case, we would conclude that google.com and bing.com are the most 
similar, with a score of 3/5 or 0.75.
"""

from collections import defaultdict
import heapq


def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

def top_pairs(log, k):

    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)

    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
        heapq.heappush(pairs, (0, ('', '')))

    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
            score = compute_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair[1] for pair in pairs]




print(top_pairs(log, 3))