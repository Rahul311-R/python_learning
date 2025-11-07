class one:
    def __init__(self):
        print("Artificial intelligence")

class two(one):
    def __init__(self):
        super().__init__()
        print("Data Science")

two()