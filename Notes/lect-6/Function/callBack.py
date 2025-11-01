

# example:
def responseMessage(message):
    print(f"Response: {message}")

def loggerInfo(message):
    print(f"Logging:{message}")


def checkPerformanceStatus(data,callback_function):
        value = data + 3.41
        print(value)
        callback_function

checkPerformanceStatus(23,loggerInfo("working Nature")) 
checkPerformanceStatus(345,responseMessage("good Nature")) 