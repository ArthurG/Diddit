# m - mc
# s - short answer 
# r - rate 1- 10 

possibleRates = list(range(1,11))
rates = map( str ,possibleRates )

possibleMC = [ "a", "b", "c", "d", "A", "B", "C", "D" ]


def DetectSpamForRate( answer ):
	if not(answer in rates): 
		return false
	else:
		return true 


def DetectSpamForMC( answer ):
	if not(answer in possibleMC):
		return false
	else:
		return true


def DetectSpamForSA( answer ):
	if len(answer) > 255:
		return false
	else:
		return true 


if (questionType = "m"):
	DetectSpamForMC(response)


if (questionType = "s"):
	DetectSpamForSA(response)


if (questionType = "r"):
	DetectSpamForRate(response)

