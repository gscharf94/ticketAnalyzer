from browser import getDict, handler, getWorkOrderTitles 
from spreadsheet import createSpreadsheet, addTitles
import time, datetime
import pickle
dateToday = datetime.date.today()

sysPATH = "C:\\Users\\Gustavo\\Documents\\Programming Stuff\\check if ready\\bin\\"
picklePath1 = sysPATH+"pickleDumps\\workOrderTickets "+str(dateToday)+".p"
picklePath2 = sysPATH+"pickleDumps\\workOrderResponses "+str(dateToday)+".p"
excelPath = sysPATH+"excelDumps\\"+str(dateToday)+" "+time.strftime("%a %I%p.xlsx")

# vv this is for testing

workOrderTickets = pickle.load(open(picklePath1,'rb'))


# VV this is what usually should be turned on

# workOrderTickets = getDict()
# pickle.dump(workOrderTickets,open(picklePath,'wb'))

# print(workOrderTickets)

workOrderResponses = {}
for workOrder in workOrderTickets:
	workOrderResponses[workOrder] = {}
	for ticket in workOrderTickets[workOrder]:
		workOrderResponses[workOrder][ticket] = []

print(workOrderResponses)

workOrderResponses.pop('131')
workOrderResponses.pop('132')
workOrderResponses.pop('124')
workOrderResponses.pop('114')
workOrderResponses.pop('111')
workOrderResponses.pop('107')
workOrderResponses.pop('129')
workOrderResponses.pop('127')
workOrderResponses.pop('118')
workOrderResponses.pop('116')
workOrderResponses.pop('121')
workOrderResponses.pop('126')
workOrderResponses.pop('125')
workOrderResponses.pop('123')
workOrderResponses.pop('128')
workOrderResponses.pop('133')


print("")

print(workOrderResponses)
# vv this is for testing
# workOrderResponses = pickle.load(open(picklePath2,'rb'))

# VV this is what usually should be turned on

workOrderResponses = handler(workOrderResponses)
# pickle.dump(workOrderResponses,open(picklePath2,'wb'))



# titleDict = getWorkOrderTitles(workOrderResponses)


# createSpreadsheet(workOrderResponses,excelPath)
# addTitles(titleDict,excelPath)