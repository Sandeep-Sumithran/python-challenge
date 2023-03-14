#imports
import csv
import os


csv_path = os.path.join("Resources", "election_data.csv")

with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    #lists
    v_id = []
    county = []
    cand_col = []

    #storing data into lists
    for rows in csvreader:
        v_id.append(rows [0])
        county.append(rows [1])
        cand_col.append(rows[2])
    
    #dictionary to gather candidate data
    dic = {}
    for cand in cand_col:
        if cand in dic:
            current_value = dic[cand]
            dic[cand] = current_value + 1
        else:
            dic[cand] = 1
    
    #calc total vtes
    total_v = len(v_id)

    #calc voter %
    elec_res = ''
    for cand in dic:
        elec_res += (cand + ": " + str(round(dic[cand]/total_v*100,3)) + "% " + "(" + str(dic[cand]) + ")\n")
    elec_res= elec_res[:-1]
    
    #identifying winner
    winner = max(dic, key = dic.get)

    #outputs
    print (f"Election Results")
    print (f"")
    print (f"----------------------")
    print (f"")
    print (f"Total Votes: {total_v}")
    print (f"")
    print (f"----------------------")
    print ("")
    print (f"{elec_res}")
    print (f"")
    print (f"----------------------")
    print (f"")
    print (f"Winner: {winner}")
    print (f"")
    print (f"----------------------")

    #text file output
    txt_file = os.path.join("Analysis", "PyPoll_Analysis.txt")

    with open(txt_file, mode= 'w') as file:
        file.write(
            f"Election Results\n"
            f"\n"
            f"----------------------\n"
            f"\n"
            f"Total Votes: {total_v}\n"
            f"\n"
            f"----------------------\n"
            "\n"
            f"{elec_res}\n"
            f"\n"
            f"----------------------\n"
            f"\n"
            f"Winner: {winner}\n"
            f"\n"
            f"----------------------\n"  
        )