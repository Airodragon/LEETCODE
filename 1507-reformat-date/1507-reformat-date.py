class Solution:
    def reformatDate(self, date: str) -> str:
        a = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        date = date.split(" ")
        ans = date[2]+"-"
        ans += a[date[1]]+"-"
        dater = ""
        for i in date[0]:
            if i.isnumeric():
                dater+=i
        if(int(dater)<10):
            ans+="0"+dater
        else:
            ans+=dater  
        return ans
        