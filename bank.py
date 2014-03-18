print('Bank Statement!')
# Practice with Lists
# MyList=['Mercury', 'Venus', 'Earth', 'Mars']
# Planet=int(input('Which planet do you want to see?'))
# print(MyList[Planet])

# Practice with Lists of Lists
# Categories = [['Comcast','Utilities'],['Meijer','Groceries'],['Trader Joes','Groceries'],['AT&T','Utilities']]
# Groceries=int(input('Comcast, Meijer, Trader Joes, or AT&T?'))
# print(Categories[Groceries])

LookupTable={}   # Apparently this creates a dictionary.
LookupTable['comcast']='Utilities'
LookupTable['meijer']='Groceries'

BankCharge=input('Where did you spend money?')
WordsInBankCharge=BankCharge.lower().split()   # Makes everything in search query lower-case and splits it into separate words for individual checking.

ChargeCategory = 'Unknown'   # At the moment I do not know the right category
for Word in WordsInBankCharge:
	if Word in LookupTable:  # If it is in the dictionary, we will change ChargeCategory
		print("       Found",Word,"in the dictionary.")
		if ChargeCategory!='Unknown':
			print('             Check Charge Category--Changed More Than Once')
			ChargeCategory = 'Error'    # Error ChargeCategory when search query includes two items in the dictionary.
		else:
			ChargeCategory = LookupTable[Word]
	else:					 # If it is not in the dictionary, we will not change ChargeCategory
		print("Did not find",Word,"in the dictionary.")

print("Final Category:", ChargeCategory)
