function [score_green_exp, score_green_order] = ...
    calc_score_for_green(Traffic_time, beta, sigma, p, NumOfCars)
% Traffic_time is a double array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. Each slot is
% the time since the last time traffic light i,j terned green. Will contain 0
% if the traffic light is red now.
% NumOfCars a 4*4 array of vectors. Each vector is of size #cars in i,j.
% Each slot in the vector contains a waiting time of car k in index i,j.  
% sigma (4*4 array), beta are scalars to learn
Ind = find(Traffic_time); % will use it to zero out green traffic lights
sigma(Ind) = 0;
Score_green_exp = sigma.*exp(beta*Traffic_time);
Score_green_order = sigma.*(Traffic_time.^p);
end