function [Score_order, score_red, score_green] =...
    calc_score(Option, NumOfCars, Traffic_time_r, Traffic_time_g)
% lambda is a double array of size 4*4 each lambda_ij is the matching scalar
% for the cars traffic light that is comming from lane i*2-1 to lane j*2
% Option is a boolean array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. if the index
% is true: this traffic light is supposed to be green in this option.
% false: red.
% NumOfCars a 4*4 cell array of cell vectors. Each vector is of size #cars in i,j.
% Each slot in the vector contains a waiting time of car k in index i,j.  
% sigma, beta and alfa are for future functions
lambda = 0.01*ones(4);
beta = 0.001;
alfa = 0.1;
p = 1;
% Runing the cars related score both exp and polinomyal
[Score_order] = calc_score_cars(lambda, Option, NumOfCars, alfa, p);
Score_order = Score_order/(10^ceil(log10(Score_order)));

sigma_r = (0.05/4)*ones(4);
beta_r = 0.01;
% Runing the traffic lights related score both exp and polinomyal
[score_red] = calc_score_for_red(Traffic_time_r, Option, beta_r, sigma_r);

sigma_g = (10/8)*ones(4);
beta_g = 0.1;
p_g = 2;

[score_green] = ...
    calc_score_for_green(Traffic_time_g, Option, beta_g, sigma_g, p_g);
end

