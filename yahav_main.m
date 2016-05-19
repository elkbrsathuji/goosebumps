function [timeToNext, option] = yahav_main(numOfCars)

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

% I'm assuming that everytime a car tern right people can walk! Hence there 
% are only 13 optimal options.

forTest = zeros(1,size(options,3));
% going over all options and choosing the maximal score
final_score = -40000*ones(1,2);
for j = 1:size(options,3)
    temp = calc_score(options(:,:,j), my_numOfCars);
    forTest(j) = temp;
    if (temp > final_score(1))
        final_score(1) = temp;
        final_score(2) = j;
    end
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
    
    
