%Determine what Delta is
%input cyc, the cycle we are interested in
%return delta, a row vector of length two with Delta_low, Delta_up
function delta = deltaFind(cyc)
    minLow = cyc(1);
    minUp = cyc(2);
    len = length(cyc);
    loop = len/2-1;
    for i = 1:loop
        if cyc(2*i+1) < minLow
            minLow = cyc(2*i+1);
        end
        if cyc(2*i+2) < minUp
            minUp = cyc(2*i+2);
        end
    end
    delta = [-1*minLow, minUp];
end
