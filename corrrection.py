import csv

def correct_csv_format():
    with open("D:\\360DT\\Course_Scanner\\new\\Code\\course.csv", 'r') as infile:
        lines = infile.readlines()

    corrected_lines = []
    current_line = ""

    for line in lines:
        if line.startswith('"'):
            current_line += line.strip('\n')
        else:
            if current_line:
                corrected_lines.append(current_line)
            current_line = line.strip('\n')
    
    if current_line:
        corrected_lines.append(current_line)

    # print(corrected_lines)
    
    with open("D:\\360DT\\Course_Scanner\\new\\Code\\course_final.csv", 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in corrected_lines:
            writer.writerow([line.split(",")[0], ','.join(line.split(",")[1:]).strip('"')])

correct_csv_format()


"""


final_data = []

with open("D:\\360DT\\Course_Scanner\\new\\Code\\course.csv", "r") as file:
    with open("D:\\360DT\\Course_Scanner\\new\\Code\\course_final.csv", "w+") as output:
        i = 1
        len_input = len(file.readlines())
        while i<n:
            


        for line in file.readlines():
            if i%2==0:
                i +=1
                continue
            i += 1
            line = line+'"'
            #print(line)
            output.write('%s\n' %line)


print("done")

"""
        
