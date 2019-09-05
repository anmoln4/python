import calendar
import datetime
import random
import attendance


def getAddress():
    return["HNo. j/7 Ghaziabad","1234567890","01441-366366"]
def getDoj():
    year=random.randrange(2000,2017)
    month=random.randrange(1,13)
    day=random.randrange(1,29)
    return datetime.date(year,month,day)
def getJobDetails(jDate):
    return attendance.getAttendance(jDate)

