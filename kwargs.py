# kwargs

#def ola(**kwargs):
#    print("Oi " + kwargs['primeiro']+ " " +kwargs['ultimo'])

#ola(primeiro="Paulo", domeio="Roberto" , ultimo="Palmeira")

def ola(**kwargs):
    print("Oi", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

ola(primeiro="Paulo", domeio="Roberto" , ultimo="Palmeira")