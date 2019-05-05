from collections import Counter


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if trust == []:
            if N == 1:
                return 1
            else:
                return -1
        people = set()
        all_people = set()
        t = []
        for l in trust:
            people.add(l[0])
            all_people.add(l[0])
            all_people.add(l[1])
            t.append(l[1])
        res = all_people - people
        if len(res) > 0:
            r = res.pop()
            if Counter(t)[r] == len(all_people) - 1:
                return r
        return -1
