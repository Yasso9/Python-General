import sys, getopt


# TYPE : python hello.py arg1 arg2 arg3
# py arguments_commandes.py hello how are you
print("1ère partie - ARGUMENTS\n")

print("List of Arguments: ", sys.argv)
print("Number of Arguments: ", len(sys.argv))
print("Currently Executing File: ", sys.argv[0])



# TYPE : python hello.py -opt1 value1 -opt2 value2
# py arguments_commandes.py -a valeur_1 -b valeur_2 -c valeur_3 hello how are you
print("\n2eme partie - OPTIONS\n")
 
argumentsListIncludingFileName = sys.argv
argumentsListExcludingFileName = argumentsListIncludingFileName[1:]

print(argumentsListIncludingFileName)
print(argumentsListExcludingFileName)
 
optionsString = "a:b:c:"
optionANDvalues, remainingArguments = getopt.getopt(argumentsListExcludingFileName, optionsString)
 
print(optionANDvalues)
print(remainingArguments)



# py arguments_commandes.py -i VALUE_i -o VALUE_o --opt1 VALUE_opt1 --some-option VALUE_some_option hello how are you
print("\n3eme partie - OPTIONS\n")

argumentsListIncludingFileName = sys.argv
argumentsListExcludingFileName = argumentsListIncludingFileName[1:]

optionsString = "i:o:"
longOptionsList = ["opt1=", "some-option="]

optionANDvalues, remainingArguments = getopt.getopt(argumentsListExcludingFileName, optionsString, longOptionsList)

print(optionANDvalues)
print(remainingArguments)

