class Notification:
    def __init__(self,message):
        self.message = message
    
    def send_message():
        pass
        
class EmailNotification(Notification):
    def __init__(self, message):
        super().__init__(message)
    
    def send_message(self):
        return f"Email: {self.message}"
    
class SMSNotification(Notification):
    def __init__(self, message):
        super().__init__(message)
    
    def send_message(self):
        return f"SMS: {self.message}"
    
class AppNotification(Notification):
    def __init__(self, message):
        super().__init__(message)
    
    def send_message(self):
        return f"APP: {self.message}"
    
message = "Today is Holiday!"
notifications = [
    EmailNotification(message),
    SMSNotification(message),
    AppNotification(message)
]

for msg in notifications:
    print()
    print(msg.send_message())
    print()