import sys

class SimpsonIntegrator(object):
    @staticmethod
    def integrate(func, a, b, desiredRelativeError):
        log2MaxFunctionEvals = 20
        return SimpsonIntegrator.simpsonIntegrate(func, a, b, desiredRelativeError, log2MaxFunctionEvals)
    
    @staticmethod
    def simpsonIntegrate(func, a, b, relativeErrorTolerance, log2MaxFunctionEvals): 
        integral = 0.0
        mostRecentContribution = 0.0
        previousContribution = 0.0
        previousIntegral = 0.0
        sum = 0.0

        functionEvalsUsed = 0.0
        estimatedError = sys.maxsize

        for stage in range(log2MaxFunctionEvals):
            if stage == 0:

                sum = func(a) + func(b)
                functionEvalsUsed = 2
                integral = sum * 0.5 * (b - a)

            else:
                numNewPts = 1 << (stage - 1)
                mostRecentContribution = 0.0
                h = (b - a) / numNewPts
                x = a + 0.5 * h

                for i in range(numNewPts):
                    mostRecentContribution += func(x + i * h)
                functionEvalsUsed += numNewPts
                mostRecentContribution *= 4.0
                sum += mostRecentContribution - 0.5 * previousContribution
                integral = sum * (b - a) / ((1 << stage) * 3.0)

                if stage >= 5:
                    estimatedError = abs(integral - previousIntegral)
                    if estimatedError <= relativeErrorTolerance * abs(previousIntegral):
                        return integral
                    
                previousContribution = mostRecentContribution
                previousIntegral = integral

        return integral