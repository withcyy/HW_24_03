class Watch:
    def __init__(self, model_name, manufacturer, year, price, watch_type):
        self.model_name = model_name
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def display_info(self):
        print("Model Name:", self.model_name)
        print("Manufacturer:", self.manufacturer)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Type:", self.watch_type)


watch = Watch("Classic", "Rolex", "2000", "2500", "Wrist")
watch.display_info()