#imports
import csv
import os
import statistics

csv_path = os.path.join("Resources", "budget_data.csv")

with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

#lists
    date_col = []
    p_l_col = []

    for rows in csvreader:
        date_col.append(rows [0])
        p_l_col.append(int(rows [1]))

#output
    t_mon = len(date_col)
    net_p = sum(p_l_col)
#change in p/l
    c_p_l = []
    for x in range(1,len(p_l_col)):
      item = p_l_col[x]
      pre_item = p_l_col[x-1]
      diff = item - pre_item
      c_p_l.append(diff)

    av_change = statistics.mean(c_p_l)

    max_c = max(c_p_l)
    i_max = c_p_l.index(max_c) + 1
    month_max = date_col[i_max]

    min_c = min(c_p_l)
    i_min = c_p_l.index(min_c) + 1
    month_min = date_col[i_min]

    def analysis():
        print (f"Financial Analysis")
        print (f"----------------------")
        print (f"Total Months: {t_mon}")
        print (f"Total: #{round(net_p)}")
        print (f"Average Change: ${round(av_change,2)}")
        print (f"Greatest Increase in Profits: {month_max} (${max_c})")
        print (f"Greatest Decrease in Profits: {month_min} (${min_c})")
        print (f"----------------------")

    analysis()

#output file
    txt_file = os.path.join("Analysis", "PyBank_Analysis.txt")

    with open(txt_file, mode= "w") as file:
        file.write(
            f"Financial Analysis\n"
            f"----------------------\n"
            f"Total Months: {t_mon}\n"
            f"Total: #{round(net_p)}\n"
            f"Average Change: ${round(av_change,2)}\n"
            f"Greatest Increase in Profits: {month_max} (${max_c})\n"
            f"Greatest Decrease in Profits: {month_min} (${min_c})\n"
            f"----------------------\n"    
        )

