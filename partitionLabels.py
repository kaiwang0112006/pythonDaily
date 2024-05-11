# -*- coding: utf-8 -*-

def solution(s):
    sdict = {}
    for i, si in enumerate(s):
        if si in sdict:
            sdict[si].append(i)
        else:
            sdict[si] = [i]

    excludestr = {}
    lo = 0
    ans = []

    for i, si in enumerate(s):
        if si not in excludestr:
            idx = max(sdict[si])
            for j in range(idx+1, len(s)):
                if sdict[s[j]][0]<= idx:
                    idx = max(sdict[s[j]][-1],idx)

            tempstr = s[lo:idx + 1]

            ans.append(len(tempstr))
            for exs in set(tempstr):
                excludestr[exs] = 1
            lo = idx + 1
    return ans

def partitionLabels(s: str):
    intervals = []
    for letter in set(s):
        left, right = s.index(letter), s.rfind(letter)
        intervals.append([left, right])
    # merge intervals
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    if not intervals:
        return [0]
    res = []
    start, end = intervals[0][0], intervals[0][1]
    for s, e in intervals[1:]:
        if end > s:
            end = max(end, e)
        else:
            res.append(end - start + 1)
            print(start,end)
            start, end = s, e
    res.append(end - start + 1)
    return res

def main():
    s = "ababcbacadefegdehijhklij"
    print(solution(s))


if __name__ == "__main__":
    main()