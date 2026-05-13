class TimeMap:

    def __init__(self):
        self.time = collections.defaultdict(list)


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:

        if key in self.time:
            newvaluetime = self.time[key]
            res = ""
            l, r = 0, len(newvaluetime) - 1
            while l <= r:
                m = (l + r) // 2
                if newvaluetime[m][0] <= timestamp:
                    res = newvaluetime[m][1]
                    l = m + 1
                else:
                    r = m - 1
            return res
        return ""
