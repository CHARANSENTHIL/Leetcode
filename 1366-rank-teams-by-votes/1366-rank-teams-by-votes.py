#                          , m is the length of vote

class Solution:
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        count = {v: [0]*len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        return "".join(sorted(votes[0], key=count.__getitem__))