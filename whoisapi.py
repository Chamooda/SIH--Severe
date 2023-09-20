import whois

def get_whois_info(domain_name):
    try:
        # Query WHOIS information for the domain
        whois_info = whois.whois(domain_name)
        
        # Print the WHOIS information
        print(whois_info)
        print(whois_info.creation_date)
        
        # You can also access specific WHOIS fields like this:
        # print("Domain Name:", whois_info.domain_name)
        # print("Registrar:", whois_info.registrar)
        # print("Creation Date:", whois_info.creation_date)
        # ...
        
    except whois.parser.PywhoisError as e:
        print("Error:", e)

# Replace 'example.com' with the domain you want to query
domain_name = 'google.com'

get_whois_info(domain_name)
