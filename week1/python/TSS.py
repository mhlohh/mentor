ftp = int(input("Enter the FTP: "))
normalizedPower = int(input("Enter the NP: "))
duration = int(input("Enter the time in minutes: "))
duration = duration * 60
intesityFactor = normalizedPower/ftp
trainingStressScore = ((duration * normalizedPower * intesityFactor)/(ftp * 3600))*100
print(trainingStressScore)