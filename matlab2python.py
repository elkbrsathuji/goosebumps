import matlab.engine
import time

st = time.time()

eng = matlab.engine.start_matlab()
tf = eng.isprime(37)
end = time.time()

print "tf", end-st