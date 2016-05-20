% stats - 4x4 matrix with proportional traffic volumes in a specific
% junction (should sum up to 1).
function [times] = roundRobin(stats)
    
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
    
    for i=1:13 
        probs(i) = sum(sum(options(:,:,i).*stats));         
    end
    
    probs = probs./sum(probs);
    
    times = roundTime*probs;
    
end