class OrderedStream:

    def __init__(self, n: int):

        self.length = n
        self.memory, self.index = {}, 1

    def insert(self, idKey: int, value: str) -> List[str]:

        self.memory[idKey] = value
        result = []

        for i in range(self.index, self.length + 1):
            if (i in self.memory):
                result.append(self.memory[i])
                self.index += 1
            else:
                break

        return (result)
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)