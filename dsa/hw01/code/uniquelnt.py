import os

class UniqueInt:
    def processFile(self, inputFilePath, outputFilePath):
       
        seen = [False] * 2047  

        
        inputFilePath = os.path.abspath(inputFilePath)
        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if line:
                    try:
                        number = int(line)
                        if -1023 <= number <= 1023:
                            seenIndex = number + 1023
                            seen[seenIndex] = True
                    except ValueError:
                        
                        continue
        
        
        outputFilePath = os.path.abspath(outputFilePath)
        with open(outputFilePath, 'w') as outputFile:
            
            for i in range(2047):
                if seen[i]:
                    integer = i - 1023
                    outputFile.write(f"{integer}\n")

if __name__ == "__main__":
    uniqueInt = UniqueInt()
    inputFilePath = r"C:\Users\julia\OneDrive\Desktop\Enterprise web\dsa_uniquelnt\dsa\hw01\sample_inputs\sample_02.txt"
    outputFilePath = r"C:\Users\julia\OneDrive\Desktop\Enterprise web\dsa_uniquelnt\dsa\hw01\sample_results\sample_outputs2.txt"
    uniqueInt.processFile(inputFilePath, outputFilePath)
