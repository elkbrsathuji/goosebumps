function [score_green] = ...
    calc_score_for_green(Traffic_time, Option, beta, sigma, p, NumOfCars)
% Traffic_time is a double array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. Each slot is
% the time since the last time traffic light i,j terned green. Will contain 0
% if the traffic light is red now.
% NumOfCars a 4*4 array of vectors. Each vector is of size #cars in i,j.
% Each slot in the vector contains a waiting time of car k in index i,j.  
% sigma (4*4 array), beta are scalars to learn
Ind = find(Traffic_time); % will use it to zero out green traffic lights
sigma(Ind) = 0;
% Bonus for being green will decay with time (target to keep it green for
% a decent amount of time)
temp_green_order = sigma.*(1/ (beta + (Traffic_time.^p)));
score_green = sum(Option.*temp_green_order);
end