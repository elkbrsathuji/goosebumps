function [timeToNext, option] = yahav_main(numOfCars, Traffic_lights)

    save('numOfCars.mat', 'numOfCars');
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

Traffic_lights_g = options*25;
Traffic_lights_r = ~options*25;
% I'm assuming that everytime a car tern right people can walk! Hence there 
% are only 13 optimal options.
load('Traffic_lights_r')
load('Traffic_lights_g')
for k = 1:size(Traffic_lights_r,3)
    car_poly = zeros(1,size(options,3));
    car_expy = zeros(1,size(options,3));
    r_poly = zeros(1,size(options,3));
    r_expy = zeros(1,size(options,3));
    g_poly = zeros(1,size(options,3));
    % going over all options and choosing the maximal score
    final_score = -40000*ones(1,4);
    for j = 1:size(options,3)
        [car_poly(j), car_expy(j), r_poly(j), r_expy(j), g_poly(j)] =...
            calc_score(options(:,:,j), my_numOfCars, Traffic_lights_r(:,:,k),...
            Traffic_lights_g(:,:,k));
        if (car_poly(j) > final_score(1))
            final_score(1) = car_poly(j);
            final_score(2) = j;
        end
        if (car_expy(j) > final_score(3))
            final_score(3) = car_expy(j);
            final_score(4) = j;
        end
        end
    end
    % when testing I want to see the score for each call
    figure; plot(1:13, car_expy)
    load('time');
    title(strcat('exp car score of each option for time: ', int2str(time)))
    figure; plot(1:13, car_poly)
    title(strcat('poly car score of each option for time: ', int2str(time)))
    figure; plot(1:13, r_poly)
    title(strcat('poly red lights score of each option for time: ', int2str(time)))
    figure; plot(1:13, r_expy)
    title(strcat('expy red lights score of each option for time: ', int2str(time)))
    figure; plot(1:13, g_poly)
    title(strcat('poly green lights score of each option for time: ', int2str(time)))
    time = time + 1;
    save('time.mat','time');
end

% creating sub options  
%     masks = zeros(4,4,16);
%     for k=0:15
%         masks(:,:,k+1) = repmat(de2bi(k,4),4,1);
%     end
%     
%     for i=1:13
%         for j=1:16
%             options(:,:,i).*masks(:,:,j)
%             calc_score(options(;,;,i).*masks(:,:,j));
%         end
%     end
end
    
    
