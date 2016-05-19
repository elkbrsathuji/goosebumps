function [score_red_exp, score_red_order] = ...
    calc_score_for_red(Traffic_time, Option, beta, sigma, p, NumOfCars)
% Traffic_time is a double array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. Each slot is
% the time since the last time traffic light i,j terned red. Will contain 0
% if the traffic light is green now.
% NumOfCars a 4*4 array of vectors. Each vector is of size #cars in i,j.
% Each slot in the vector contains a waiting time of car k in index i,j.  
% sigma (4*4 array), beta are scalars to learn
Ind = find(Traffic_time); % will use it to zero out green traffic lights
sigma(Ind) = 0;
temp_red_exp = sigma.*exp(beta*Traffic_time);
temp_red_order = sigma.*(Traffic_time.^p);

score_red_exp = sum(Option.*temp_red_exp);
score_red_order = sum(Option.*temp_red_order);
end