class Website:
    def __init__(self, name, address, description):
        self.name = name
        self.address = address
        self.description = description

    def display_info(self):
        print("Website Name:", self.name)
        print("Address:", self.address)
        print("Description:", self.description)

website = Website("My_stat", "https://My_stat.com", "School dictionary")
website.display_info()