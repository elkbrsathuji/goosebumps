    my_numOfCars = cell(4,4);
    for i = 1:4
        my_numOfCars(:,i) = numOfCars{1,i};
    end
    timeToNext = 10; % It's going to be static
    options = zeros(4,4,13);
    options(:,:,1) = [0,0,1,1;0,0,0,0;1,1,0,0;0,0,0,0];
    options(:,:,2) = [0,0,0,0;1,0,0,1;0,0,0,0;0,1,1,0];
    options(:,:,3) = [0,1,0,0;1,0,0,0;0,0,0,1;0,0,1,0];
    options(:,:,4) = [0,0,0,1;0,0,1,0;0,1,0,0;1,0,0,0];
    options(:,:,5) = [0,0,0,0;0,0,0,0;1,1,0,1;0,0,1,0];
    options(:,:,6) = [0,0,0,1;0,0,0,0;0,0,0,0;1,1,1,0];
    options(:,:,7) = [0,1,1,1;1,0,0,0;0,0,0,0;0,0,0,0];
    options(:,:,8) = [0,0,0,0;1,0,1,1;0,1,0,0;0,0,0,0];
    options(:,:,9) = [0,0,0,1;1,0,0,0;0,1,0,0;0,0,1,0];
    options(:,:,10) = [0,0,1,1;1,0,0,0;0,1,0,0;0,0,0,0];
    options(:,:,11) = [0,0,0,0;1,0,0,1;0,1,0,0;0,0,1,0];
    options(:,:,12) = [0,0,0,1;0,0,0,0;1,1,0,0;0,0,1,0];
    options(:,:,13) = [0,0,0,1;1,0,0,0;0,0,0,0;0,1,1,0];

% I'm assuming that everytime a car tern right people can walk! Hence there 
% are only 13 optimal options.

forTest_poly = zeros(1,size(options,3));
forTest_expy = zeros(1,size(options,3));
% going over all options and choosing the maximal score
final_score = -40000*ones(1,4);
for j = 1:size(options,3)
    poly = calc_score(options(:,:,j), my_numOfCars, true);
    expy = calc_score(options(:,:,j), my_numOfCars, false);
    forTest_poly(j) = ploy;
    forTest_expy(j) = expy;
    if (poly > final_score(1))
        final_score(1) = poly;
        final_score(2) = j;
    end
    if (expy > final_score(3))
        final_score(3) = expy;
        final_score(4) = j;
    end
end
% when testing I want to see the score for each call
figure; plot(1:13, forTest_expy, 1:13, forTest_poly)
load('time');
title(strcat('score of each option for time: ', int2str(time)))