# re is python library regex, install with 'pip install regex'
import re;

# Read file into reader variable
def parseFile(_fileToReadPath):
    _arrayToStoreDataIn = [];
    file = open(_fileToReadPath);
    try:
        for line in file: # Iterate through each line, storing data found between ':' and ';' in result
            result = re.search(':(.*);', line);
            _arrayToStoreDataIn.append(result.group(1)); # Store data in storage array
    finally: # Close the file once reading is complete
            file.close()

    return _arrayToStoreDataIn;
