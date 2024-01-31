
#Dictionary and counter in Python to find the winner of the election

from collections import Counter

def find_winner(votes):
    vote_count = Counter(votes)
    winner = vote_count.most_common(1)[0][0]
    return winner

# Example
votes = ['A', 'B', 'A', 'C', 'B', 'A']
result = find_winner(votes)
print(result)
