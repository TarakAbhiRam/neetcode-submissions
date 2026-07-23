class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.storage:
            return ""
        values = self.storage[key]
        #linear search
        for i in values:
            ans=''
            if i[1] <= timestamp:
                res = i[0]
            else:
                break
        return res


        
