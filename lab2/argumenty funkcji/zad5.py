
def make_car(firma, model, **kwargs):
    dict = {"firma" : firma, "model" : model}
    dict.update(kwargs)
    return dict

print("zadanie 5:\nsamochód 1: ", make_car("Kia","Picanto",kolor="cafe mocca", poj_silnika=900))
print("samochód 2: ", make_car("Toyota","Corolla",kolor="biały", rodzaj="sportowy"))
print("samochód 3: ", make_car("Kia","Rio",kolor="niebieski", rok=2005))