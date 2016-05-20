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

Traffic_lights_g = options*10;
Traffic_lights_r = ~options*10;
% I'm assuming that everytime a car tern right people can walk! Hence there 
% are only 13 optimal options.
% load('Traffic_lights_r')
% load('Traffic_lights_g')
for k = 1:size(Traffic_lights_r,3)
    a = cell(4,4);
    for x = 1:4
        for y = 1:4
            if (x == y)
              a(x,y) = mat2cell([0],1,1);
            else
            a(x,y) = mat2cell(rand(1,length(my_numOfCars{x,y}))*100, 1, length(my_numOfCars{x,y}));
            end
        end
    end
    car_poly = zeros(1,size(options,3));
    car_expy = zeros(1,size(options,3));
    r_expy = zeros(1,size(options,3));
    g_poly = zeros(1,size(options,3));
    % going over all options and choosing the maximal score
    final_score = -40000*ones(1,4);
    for j = 1:size(options,3)
        [car_poly(j), car_expy(j), r_expy(j), g_poly(j)] =...
            calc_score(options(:,:,j), a, Traffic_lights_r(:,:,k),...
            Traffic_lights_g(:,:,k));

    end
    % when testing I want to see the score for each call
    load('time');
    figure; plot(1:13, car_expy)
    title(strcat('exp car score of each option for time: ', int2str(time)))
    figure; plot(1:13, car_poly)
    title(strcat('poly car score of each option for time: ', int2str(time)))
%     figure; plot(1:13, r_expy)
%     title(strcat('expy red lights score of each option for time: ', int2str(time)))
%    figure; plot(1:13, g_poly)
%     title(strcat('poly green lights score of each option for time: ', int2str(time)))
%     time = time + 1;
end
