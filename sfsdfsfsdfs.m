    Traffic_lights_on = zeros(4,4,1);
    Traffic_lights_time = zeros(4,4,1);
    for v = 1:4
        for u = 1:4
            temp = Traffic_lights{1,v};
            temp = temp{1,u};
            Traffic_lights_on(v,u,1) = temp{1};
            Traffic_lights_time(v,u,1) = temp{2};
        end
    end