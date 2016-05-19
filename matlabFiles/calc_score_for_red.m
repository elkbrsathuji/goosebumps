function [Score] = calc_score_for_red(Traffic, NumOfCars, beta, alfa, p)
% lambda is a double array of size 4*4 each lambda_ij is the matching scalar
% for the cars traffic light that is comming from lane i*2-1 to lane j*2
% Option is a boolean array of size 4*4 each index - i,j reffering to
% a traffic light that is comming from lane i*2-1 to lane j*2. if the index
% is true: this traffic light is supposed to be green in this option.
% false: red.
% NumOfCars a 4*4 array of vectors. Each vector is of size #cars in i,j.
% Each slot in the vector contains a waiting time of car k in index i,j.  
% sigma, beta and alfa are for future functions
[rows cols] = find(Option);
my_weight = 0;
my_weight_exp = 0;
% performing the calculation: lambda(i)*e^(beta*sum(waiting time of i))
% for all green lanes in this permutation.
for i = 1:length(rows)
    my_weight_exp = my_weight_exp + lambda(rows(i), cols(i))*...
        exp(beta*sum(NumOfCars(rows(i), cols(i))));
    my_weight = my_weight + lambda(rows(i), cols(i))*...
        sum((NumOfCars(rows(i), cols(i)).^p));
end
[rows_other cols_other] = find(Option == 0);
other_weight = 0;
other_weight_exp = 0;
% performing the same calcaulation for all red lanes in this permutation.
for i = 1:length(rows_other)
    other_weight_exp = other_weight_exp + lambda(rows_other(i), cols_other(i))*...
        exp(alfa*sum(NumOfCars(rows_other(i), cols_other(i))));
    other_weight = other_weight + lambda(rows_other(i), cols_other(i))*...
        sum((NumOfCars(rows_other(i), cols_other(i)).^p));
end
score_order = my_weight - other_weight;
score_exp = my_weight_exp - other_weight_exp;
end