class Solution:
    def intervalIntersection(self, A, B):
        result  = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            minA, maxA = A[i]
            minB, maxB = B[j]
            # there is no interesection - take next interval from A
            if maxA < minB:
                i += 1
                continue  
            else:
                start = max(minA, minB)
                stop = min(maxA, maxB)
                # interval intersection condition
                if start <= stop:
                    result.append([start, stop])
            # take next interval from A
            if maxA < maxB:
                i += 1
            # take next interval from B
            else:
                j += 1
        return result
