from myhaversine import myhaversine
from haversine import haversine



def test_haversine():
    lyon = (45.7597, 4.8422)
    paris = (48.8567, 2.3508)

    calc_1 =  myhaversine(lyon, paris)
    calc_2 = haversine(lyon, paris)
    diff = abs(calc_1 - calc_2)
    assert diff <= 0.01, "La diferencia es mayor que 0.01 (10m)"


