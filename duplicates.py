import csv
import os

def combine_csv_files(input_files, output_file):
    # Check if all input files exist
    for file in input_files:
        if not os.path.exists(file):
            print(f"Error: File '{file}' does not exist.")
            return

    # Read the first file to get the headers
    with open(input_files[0], 'r', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)

    # Write to the output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)  # Write the headers

        # Process each input file
        for file in input_files:
            with open(file, 'r', newline='') as infile:
                reader = csv.reader(infile)
                next(reader)  # Skip the header row
                for row in reader:
                    writer.writerow(row)

    print(f"Combined CSV file created: {output_file}")

# Example usage
# input_files = ['posts_foryou.csv', 'posts_nearby.csv', 'posts_recent.csv']
# output_file = 'combined_output.csv'

# combine_csv_files(input_files, output_file)



def remove_duplicates_from_csv(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    # Read the CSV file and store unique rows
    unique_rows = set()
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Read the header row
        for row in reader:
            unique_rows.add(tuple(row))  # Convert row to tuple for hashability

    # Write unique rows to the output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)  # Write the header row
        writer.writerows(unique_rows)  # Write unique rows

    print(f"Duplicates removed. Output file created: {output_file}")
    print(f"Original row count: {len(unique_rows) + 1}")  # +1 for header
    print(f"Unique row count: {len(unique_rows)}")

# Example usage
input_file = 'input.csv'
output_file = 'output_no_duplicates.csv'

#remove_duplicates_from_csv("combined_output.csv", "nextdoor_cleaned.csv")

###

# import pandas as pd

# # Function to remove duplicates from a CSV file
# def remove_duplicates(input_file, output_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(input_file)
    
#     # Drop duplicate rows
#     df_cleaned = df.drop_duplicates()
    
#     # Save the cleaned DataFrame back to a new CSV file
#     df_cleaned.to_csv(output_file, index=False)
    
#     print(f"Duplicates removed. Cleaned data saved to {output_file}")

# # Example usage
# input_file = 'combined_output.csv'  # Replace with your input CSV file
# output_file = 'output_file.csv'  # Replace with your desired output CSV file
# remove_duplicates(input_file, output_file)



import csv
import sys

def transform_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile, delimiter=';')
            writer = csv.writer(outfile, delimiter=',')
            
            for row in reader:
                writer.writerow(row)
        
        print(f"Successfully transformed {input_file} to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read {input_file} or write to {output_file}.")
    except csv.Error as e:
        print(f"CSV Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


transform_csv("nextdoor_cleaned.csv", "nextdoor_cleanedv1.csv")



