class MyCalendar:

    def __init__(self):
        self.ans = []

    def book(self, start: int, end: int) -> bool:
        for i in self.ans:
            if end>i[0] and start<i[1]:
                return False
        self.ans.append([start,end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)