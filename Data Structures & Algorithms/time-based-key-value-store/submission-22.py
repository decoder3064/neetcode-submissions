class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value, timestamp))
        else:
            self.d[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        to_parse = self.d[key]
    
        if timestamp < to_parse[0][1]:
            return ""

        if len(to_parse) == 1: 
            return to_parse[0][0]
         
        l = 0
        r = len(to_parse)-1

        while l < r: 
            mid = int(math.ceil((l+r)/2))
            stamp = to_parse[mid]

            if stamp[1] > timestamp: 
                r = mid-1 
            elif stamp[1] < timestamp: 
                l = mid
            else:
                return stamp[0]
            

        return to_parse[l][0]


            







        
