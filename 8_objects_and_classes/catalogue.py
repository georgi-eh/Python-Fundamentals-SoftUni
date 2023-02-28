class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        filtered_products = []
        for product in self.products:
            if product[0] == first_letter:
                filtered_products.append(product)
        return filtered_products

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + "\n".join(sorted(self.products))
