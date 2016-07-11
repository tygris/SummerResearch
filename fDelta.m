%This function finds the value of f(Delta)
%It is a helper function for fPlot
%by Natalie Wellen
%
%input cyc, the cycle we are looking to update
%input eta, the matrix of ij indicies for the cycle (row1 = i row2 = j),
%           must be in order
%input p, the probability matrix of our model
%input lambda, the parameter matrix of our model
%input x, The value of Delta
%output y, The value of f(Delta)
function y = fDelta(cyc, eta, p, lambda, x)
    y = 1; %since we are multiplying 1 is our identity
    twok = length(cyc);
    k=twok/2;
    for i=1:k    %instead of 1:2*k we check two indices at a time
        if (cyc(2*i-1)+x)<=1.0*10^(-50)        %the odd entries of the cycle, within margin of error if is zero
            y = y*(1-p(eta(1,i),eta(2,i)));
        elseif (cyc(2*i-1)+x)>0                %The if statements are the indicator functions
            y = y*( p(eta(1,i),eta(2,i))*lambda(eta(1,i),eta(2,i))*exp( -1*lambda(eta(1,i),eta(2,i))*(cyc(2*i-1)+x) ) );
        else
            y = 0;
            break;
        end
        if (cyc(2*i)-x)<=1.0*10^(-50)          %the even entries of the cycle, within margin of error is zero
            y = y*(1-p(eta(1,i),eta(2,mod(i,k)+1)));
        elseif (cyc(2*i)-x)>0
            y = y*( p(eta(1,i),eta(2,mod(i,k)+1))*lambda(eta(1,i),eta(2,mod(i,k)+1))*exp( -1*lambda(eta(1,i),eta(2,mod(i,k)+1))*(cyc(2*i)-x) ) );
        else
            y = 0;
            break;
        end
    end
end

%for future, check matrix dimensions/ create matrix for p and lambda