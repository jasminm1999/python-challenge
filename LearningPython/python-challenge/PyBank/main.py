import os
import csv


# path to CSV file
csv_path = os.path.join("LearningPython/python-challenge/PyBank/Resources/budget_data.csv")

# variables for results 
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# read the csv file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    for row in csvreader:
        total_months += 1

        # calculate total "profit/losses"
        total_profit_loss += int(row[1])

        # track changes
        profit_loss = int(row[1])
        profit_loss_change = profit_loss - previous_profit_loss


        if total_months > 1:
            profit_loss_changes.append(profit_loss_change)
            dates.append(row[0])

        previous_profit_loss = profit_loss

    # calculate average change in "profit/losses"
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)

    # find greatest increase and decrease in profits
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    increase_date = dates[profit_loss_changes.index(greatest_increase)]
    decrease_date = dates[profit_loss_changes.index(greatest_decrease)]



    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change: .2f}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")


    # export results to text file
    output_path = os.path.join("LearningPython/python-challenge/PyBank/analysis/financial_analysis.txt")
    with open(output_path, "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("------------------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${total_profit_loss}\n")  
        txtfile.write(f"Average Change: ${average_change: .2f}\n") 
        txtfile.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

    print(f"Results have been written to the '{output_path}' file.")





