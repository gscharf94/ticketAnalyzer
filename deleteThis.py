f = open('deleteThis.txt','r')

text = f.read()

f.close()

# print(text)

temp = text


listy = []

while True:
	index = temp.find('"text-overflow-2"><!----> ')
	if index == -1:
		break
	else:
		temp = temp[index+26:len(temp)]
		endIndex = temp.find("</div>")
		chunk = temp[0:endIndex-1]
		listy.append(chunk)
		temp = temp[endIndex:len(temp)]

listy2 = []

temp2 = text

# bigIndex = temp2.find('<div id="cdk-describedby-message-container" aria-hidden="true" style="display: none;">')
# temp2 = temp2[bigIndex+86:len(temp2)]


while True:
	index = temp2.find('class="text-overflow-1 ng-star-inserted">')
	if index == -1:
		break
	else:
		temp2 = temp2[index+41:len(temp2)]
		endIndex = temp2.find("<")
		chunk = temp2[0:endIndex]
		listy2.append(chunk)
		temp2 = temp2[endIndex:len(temp2)]

print(listy)
print("")
print(listy2)