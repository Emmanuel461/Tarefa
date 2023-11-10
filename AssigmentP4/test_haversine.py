from myhaversine import myhaversine
from haversine import haversine

def test_haversine():
    lyon = (45.7597, 4.8422)
    paris = (48.8567, 2.3508)
    santiago = ( -33.45, -70.67)
    north_pole =  (90,0)

    calc_LP_1 =  myhaversine(lyon, paris)
    calc_LP_2 = haversine(lyon, paris)
    diff_L_P = abs(calc_LP_1 - calc_LP_2)
    assert diff_L_P <= 0.01, "La diferencia entre el cálculo de Lyon y el Paris es mayor que 0.01 (10m)"

    calc_SNP_1 =  myhaversine(santiago, north_pole)
    calc_SNP_2 = haversine(santiago, north_pole)
    diff_S_NP = abs(calc_SNP_1 - calc_SNP_2)
    assert diff_S_NP <= 0.02, "La diferencia entre el cálculo de Santiago y el Polo Norte es mayor que 0.01 (10m)"

from myfunctions import mysqrt # TROCAS TROCAS 
import math 

def test_mysqrt():
    a = mysqrt(16)  
    b = math.sqrt(16)
    diff_sqrt = abs(a-b)
    assert diff_sqrt <= 0.001

from myhaversine import mysin

def test_mysin():
    a = mysin(45)
    b = math.sin(45)
    diff_sin_1 = abs(a-b)
    a1 = mysin(180)
    b1 = math.sin(180)
    diff_sin_2 = abs(a-b)
    assert diff_sin_1 <= 1.5
    assert diff_sin_2 <= 1.5
