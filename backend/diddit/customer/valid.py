# m - mc
# s - short answer 
# r - rate 1- 10 
import sys 

possibleRates = list(range(1,11))
rates = map( str ,possibleRates )

possibleMC = [ "a", "b", "c", "d", "A", "B", "C", "D" ]


def DetectSpamForRate( answer ):
	if not(answer in rates): 
		return False
	else:
		return True 


def DetectSpamForMC( answer ):
	if not(answer in possibleMC):
		return False
	else:
		return True


def DetectSpamForSA( answer ):
	if len(answer) > 255:
		return False
	else:
		return True 


def main(response, questionType):

	if (questionType == "m"):
		x = DetectSpamForMC(response)
		return x

	if (questionType == "s"):
		y = DetectSpamForSA(response)
		return y

	if (questionType == "r"):
		z = DetectSpamForRate(response)
		return z




if __name__ == "__main__":
    # execute only if run as a script
    argsLen = len(sys.argv)
    response = sys.argv[1]
    questionType = sys.argv[2]

    if (argsLen > 2):
    	yo = main(response , questionType)
    	print yo
    	