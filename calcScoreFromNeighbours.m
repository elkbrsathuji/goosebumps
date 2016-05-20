% neighbours - A (4x4x2) cell array with entrances:
% 1st - Entring lane
% 2nd - Exit lane
% 3rd - (How many cars are coming, From which distance)
function [polyScore] = calcScoreFromNeighbours(option, neighbours, d, alpha)
    polyScore = alpha*option.*neighbours(:,:,1).*(1./(neighbours(:,:,2).^d));
end