% stats - 4x4 matrix with proportional traffic volumes in a specific
% junction (should sum up to 1).
function [option] = roundRobin(stats, time)
    
    roundTime = 2*60;

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
   
    %masks = zeros(4,4,16);
    %for k=0:15
    %    masks(:,:,k+1) = repmat(de2bi(k,4),4,1);
    %end
    
    probs = zeros(13,1);
    stats_mat = cell(4,4);
    for i = 1:4
        stats_mat(:,i) = stats{1,i};
    end
    for i=1:13 
        probs(i) = sum(sum(options(:,:,i).*cell2mat(stats_mat)));         
    end
    
    probs = probs./sum(probs);
    times = roundTime*probs;
    
    modTime = mod(time, roundTime);
    
    i = 1;
    temp = modTime - times(i);
    
    while(temp > 0)
       i = i + 1;
       temp = temp - times(i);    
    end
    
    option = options(:,:,i);
end