# your code goes here!
import re 

class EmailAddressParser:
    def __init__(self, string):
        self.email_address = string

    def parse(self):
        pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        addresses = re.split(r"[,\s]+", self.email_address)
        unique_addresses = sorted(set(filter(lambda address: re.match(pattern, address.strip()), addresses)))
        return unique_addresses