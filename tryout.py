from ntpath import join


lines = []
with open("pizza_input.txt") as f:
    lines = f.readlines() 
    line = lines[0]   
    splitLine = line.split(' ')
    firstVar = "pizza"
    
    availablePizzas = splitLine[0]
    output = availablePizzas +"\n"
    for j in range(len(splitLine)):
       
        t2 = splitLine[1]
        t3 = splitLine[2]
        t4 = splitLine[3]
        #print(availablePizzas+t2+t3+t4)
        
        output += firstVar+" " + " ".join(splitLine)

        print(output)

    for i in range(len(lines)):
        pass

    with open('output_file.txt', 'w') as wf:
        output = "this is the output"
        output2 = "this is the second line"
        outputFileText = output + "\n" 
        outputFileText += output2
        wf.write(outputFileText)
        





#print(len(lines))

# count = 0
# for line in lines:
#     count += 1
#     print(f'line {count}: {line}')