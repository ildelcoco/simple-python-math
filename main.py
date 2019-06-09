from SimpsonIntegrator import SimpsonIntegrator
import math

def targetFunction(x): 
    return math.sin((3 * x) / 2) + 1 / 2

integral = SimpsonIntegrator.integrate(targetFunction, 0, math.pi, 0.001)

print(integral)