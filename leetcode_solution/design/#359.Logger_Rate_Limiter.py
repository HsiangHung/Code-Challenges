# 
# #359. Logger Rate Limiter
#
#
class Logger(object):

    def __init__(self):
        self.allow_logs = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.allow_logs:
            self.allow_logs[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.allow_logs[message]:
                self.allow_logs[message] = timestamp + 10
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)