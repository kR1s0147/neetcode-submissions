class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timemap:
            self.timemap[key] = {}
        

        if timestamp  not in self.timemap[key].keys():
            self.timemap[key][timestamp] = []
        

        self.timemap[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap :
            return ""
        
        timestamps = list(self.timemap[key].keys())
        timestamps.sort(reverse = True)
        for time in timestamps:
            if time <= timestamp:
                return self.timemap[key][time][-1]
        return ""
