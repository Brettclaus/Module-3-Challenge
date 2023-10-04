import os
import csv

# Path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Path to the output text file in the analysis folder
output_file = os.path.join("analysis", "financial_analysis.txt")

# Initialize variables
total_profit_loss = 0           # Total profit/loss
unique_months = set()           # Set to store unique months, I know we didn't have to do this but I misinterpreted this part of the assignment initially and figured I'd keep this! 
months = []                      # List to store all months
profit_losses = []              # List to store changes in profit/loss
previous_value = None           # Store the previous month's profit/loss
max_increase = float("-inf")    # Initialize with negative infinity for maximum increase
max_decrease = float("inf")     # Initialize with positive infinity for maximum decrease
max_increase_date = None        # Store the date of the maximum increase
max_decrease_date = None        # Store the date of the maximum decrease

# Open the CSV file for reading
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader, None)

    # Loop through the CSV data
    for row in csvreader:
        # Calculate the total profit/loss by adding values from the second column
        total_profit_loss += int(row[1])

        # Extract and add the month part to unique_months and months list
        date_parts = row[0].split("-")
        if len(date_parts) >= 1:
            month = date_parts[0]
            unique_months.add(month)
            months.append(month)

        # Calculate the change in profit/loss from the previous month
        current_value = int(row[1])
        if previous_value is not None:
            change = current_value - previous_value
            profit_losses.append(change)
            
            # Check for maximum increase and decrease
            if change > max_increase:
                max_increase = change
                max_increase_date = row[0]
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = row[0]
        previous_value = current_value

# Calculate the average change
average_change = sum(profit_losses) / len(profit_losses)

# Format as currency
formatted_total_profit_loss = '${:,.2f}'.format(total_profit_loss)
formatted_average_change = '${:,.2f}'.format(average_change)
formatted_max_increase = '${:,.2f}'.format(max_increase)
formatted_max_decrease = '${:,.2f}'.format(max_decrease)

# Print financial analysis
print("\n\nFinancial Analysis")
print("----------------------------------------\n\n")
print("Total Months:", len(months))
print("\nTotal Profit/Loss:", formatted_total_profit_loss)
print("\nNumber of unique months:", len(unique_months))
print("\nAverage Change in Profit/Loss:", formatted_average_change)
print("\nGreatest Increase in Profits:", max_increase_date, '(', formatted_max_increase, ')')
print("\nGreatest Decrease in Profits:", max_decrease_date, '(', formatted_max_decrease, ')\n')

# Create and write the financial analysis to the output text file
with open(output_file, "w") as txtfile:
    txtfile.write("\n\nFinancial Analysis\n")
    txtfile.write("----------------------------------------\n\n")
    txtfile.write("Total Months: {}\n".format(len(months)))
    txtfile.write("Total Profit/Loss: {}\n".format(formatted_total_profit_loss))
    txtfile.write("Number of unique months: {}\n".format(len(unique_months)))
    txtfile.write("Average Change in Profit/Loss: {}\n".format(formatted_average_change))
    txtfile.write("Greatest Increase in Profits: {} ({})\n".format(max_increase_date, formatted_max_increase))
    txtfile.write("Greatest Decrease in Profits: {} ({})\n".format(max_decrease_date, formatted_max_decrease))

# Print a message that the analysis has been saved
print("Financial analysis has been saved to:", output_file)
