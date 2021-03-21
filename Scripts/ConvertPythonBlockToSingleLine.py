def convert(fname):
    newLines = ''
    with open(fname, 'r') as f:
        for line in f:
            num_spaces = 0
            
            for letter in line:
                if letter != ' ':
                    break
                num_spaces += 1
            print('Number Of Spaces : ', num_spaces)       

            if num_spaces == 3:
                line = line.replace(' '*3, '\\t') #If number of Spaces is 3, replace with a single tab
            elif num_spaces == 4:
                line = line.replace(' '*4, '\\t') #If number of Spaces is 4, replace with a single tab
            elif num_spaces == 7:
                line = line.replace(' ' *7, '\\t\\t') #If number of Spaces is 7, replace with double tab
            elif num_spaces == 8:
                line = line.replace(' ' * 8, '\\t\\t') #If number of Spaces is 8, replace with double tab
            #line = line + '\\n' #Adding new line at the end of the line
            newLines = newLines + line
            
    converted = repr(newLines)
    print(converted)
    return converted

def convertTargetToSingleLine(block):
    lines = block.splitlines()
    newLines = ''
    for line in lines:
            num_spaces = 0
            
            for letter in line:
                if letter != ' ':
                    break
                num_spaces += 1
            print('Number Of Spaces : ', num_spaces)       

            if num_spaces % 12 == 0:
                line = line.replace(' '*12, '\\t\\t\\t') #If number of Spaces is 12, replace with triple tab
            elif num_spaces % 11 == 0:
                line = line.replace(' '*11, '\\t\\t\\t') #If number of Spaces is 11, replace with triple tab
            elif num_spaces % 8 == 0:
                line = line.replace(' '*8, '\\t\\t') #If number of Spaces is 8, replace with double tab
            elif num_spaces % 7 == 0:
                line = line.replace(' '*7, '\\t\\t') #If number of Spaces is 7, replace with a double tab
            elif num_spaces % 4 == 0:
                line = line.replace(' ' *4, '\\t') #If number of Spaces is 4, replace with single tab
            elif num_spaces % 3 == 0:
                line = line.replace(' ' * 3, '\\t') #If number of Spaces is 3, replace with a single tab
            newLines = newLines + '\n' +  line
            
    converted = repr(newLines)
    return converted
    
    

