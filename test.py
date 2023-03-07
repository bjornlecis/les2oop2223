class Ding:

    def __init__(self):
        self.info =  "DIT IS EEN DING"
    def __str__(self):
        return self.info

ding = Ding()
ding.info = "de info is anders nu"
print(ding)
