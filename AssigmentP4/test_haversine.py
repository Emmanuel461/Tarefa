from myhaversine import myhaversine
from haversine import haversine



def test_haversine():
    lyon = (45.7597, 4.8422)
    paris = (48.8567, 2.3508)

    calc_1 =  myhaversine(lyon, paris)
    calc_2 = haversine(lyon, paris)
    try:
        diff = abs(float(calc_1 - calc_2))
        assert diff <= 0.01
    except AssertionError:
        print("La diferencia es más de 0.01 km (10 metros)")

