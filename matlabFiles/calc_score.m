function [Score] = calc_score(Option, NumOfCars, Traffic_time_r, Traffic_time_g)
% lambda is a double array of size 4*4 each lambda_ij is the matching scalar
% for the cars traffic light that is comming from lane i*2-1 to lane j*2
% Option is a boolean array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. if the index
% is true: this traffic light is supposed to be green in this option.
% false: red.
% NumOfCars a 4*4 array of vectors. Each vector is of size #cars in i,j.
% Each slot in the vector contains a waiting time of car k in index i,j.  
% sigma, beta and alfa are for future functions
lambda = ones(4);
sigma_r = ones(4);
sigma_g = ones(4);
beta = 1;
alfa = 1;
beta_r = 1;
beta_g = 1;
p = 2;
p_r = 2;
p_g = 2;
% Runing the cars related score both exp and polinomyal
[Score_exp, Score_order] = calc_score_cars(lambda, Option, NumOfCars, beta, alfa, p);
% Runing the traffic lights related score both exp and polinomyal
[score_red_exp, score_red_order] = ...
    calc_score_for_red(Traffic_time_r, Option, beta_r, sigma_r, p_r);
[score_green_exp, score_green_order] = ...
    calc_score_for_green(Traffic_time_g, Option, beta_g, sigma_g, p_g);

end

