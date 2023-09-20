import csv

domain_list =[]
mal_domain_list=[]

csv_file_path = "top-1m.csv"
mal_csv_file_path = "verified_online.csv"

def addToList(csv_file_path,domain_list):
    with open(csv_file_path, mode='r', newline='',encoding='utf-8') as file:
        
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
        if item == input_str:
            return 1
        elif(is_one_char_change(input_str, item)):
            return 2
    return 0

# Input string to check
current_domain = "http://widi.159-203-94-52.cprapid.com"

addToList(csv_file_path,domain_list)
addToList(mal_csv_file_path,mal_domain_list)

if string_belongs_to_list(current_domain, domain_list)==1:
    print(f"'{current_domain}' is top domain")
elif string_belongs_to_list(current_domain, mal_domain_list)==1:
    print(f"'{current_domain}' is a phishing domain")
elif string_belongs_to_list(current_domain, domain_list)==2:
    print(f"'{current_domain}' is a typo")
else:
    print(f"'{current_domain}' not a typo")
