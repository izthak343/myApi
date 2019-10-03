

def sum(firstNum,secondNum):
	ansArray=[]
	carry=0;
	#find the logest and the small number 
	if(len(firstNum)>len(secondNum)):
		lenBig=len(firstNum)
		lenSmall=len(secondNum)
		big=firstNum
		small=secondNum
	else:
		lenBig=len(secondNum)
		lenSmall=len(firstNum)
		big=secondNum
		small=firstNum

	indexSmall=lenSmall-1
	#sum the numbers from end to start [1,2,3] == 123
	for i in range(lenBig-1,-1,-1):
		if indexSmall <=- 1:
			addDigit=0
		else:
			addDigit=small[indexSmall]
		#case there is a carry
		if carry==1:
			addDigit+=1
			carry=0
		sumNum=big[i]+addDigit
		if(sumNum>9):
			carry=1;
		ansArray.insert(0,(sumNum%10))
		indexSmall-=1
	#case there is a carry in the last sum 
	if(carry==1):
		ansArray.insert(0,carry)
	return ansArray

def multiply(firstNum,secondNum):
	if(firstNum == [0] or secondNum == [0]):
		return [0]
	longNumberArray=[]
	carry=0

	#find the logest and the small number
	if(len(firstNum)>len(secondNum)):
		lenBig=len(firstNum)
		lenSmall=len(secondNum)
		big=firstNum
		small=secondNum
	else:
		lenBig=len(secondNum)
		lenSmall=len(firstNum)
		big=secondNum
		small=firstNum
	#multiply the numbers from end to start [1,2,3] == 123
	for i in range(lenSmall-1,-1,-1):
		digitArray=[]
		for j in range(lenBig-1,-1,-1):
			multiplyNum=small[i]*big[j]+carry
			carry=0
			if multiplyNum>9:
				carry=int(multiplyNum//10)
			digitArray.insert(0,multiplyNum%10)
		#case there is a carry
		if carry!=0:
			digitArray.insert(0,carry)
			carry=0
		for j in range(len(longNumberArray)):
			digitArray.append(0)
		longNumberArray.append(digitArray)
	ansArray=[]
	for digitArray in longNumberArray:
		ansArray=sum(ansArray,digitArray)
	return ansArray;