function [Score] = calc_score(lambda, Option, NumOfCars, sigma, beta, alfa)
% lambda is a double array of size 4*4 each lambda_ij is the matching scalar
% for the cars traffic light that is comming from lane i*2-1 to lane j*2
% Option is a boolean array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. if the index
% is true: this traffic light is supposed to be green in this option.
% false: red.
% NumOfCars a 4*4 array of vectors of size 2*1. In each vector; the first index
% contains the sum of waiting time, the second contains #cars waiting.  
% sigma, beta and alfa are for future functions
Score = lambda()



end
