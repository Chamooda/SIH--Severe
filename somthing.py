import csv

domain_list =[]

csv_file_path = "top200.csv"

with open(csv_file_path, mode='r', newline='') as file:
    
    csv_reader = csv.DictReader(file)

    for row in csv_reader:

        domain = row["domain"]
        domain_list.append(domain)

#print(domain_list)

def is_one_char_change(str1, str2):
    """
    Check if two strings are one character change away.
    """
    if len(str1) != len(str2):
        return False

    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
            if diff_count > 1:
                return False

    return diff_count == 1

def string_belongs_to_list(input_str, string_list):
    """
    Check if input_str belongs to a list of strings with one character change.
    """
    for item in string_list:
        if is_one_char_change(input_str, item):
            return True
    return False

# Input string to check
current_domain = "goggle.com"

if string_belongs_to_list(current_domain, domain_list):
    print(f"'{current_domain}' could be a typo")
else:
    print(f"'{current_domain}' not a typo")
