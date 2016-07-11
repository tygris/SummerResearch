%This function is f* in Algorithm 1 of Gandy&Veraart 2016
%It makes a plotable vector of the values in Delta's range
%
%input cyc, the cycle we are looking to update
%input eta, the matrix of ij indicies for the cycle 
%input p, the probability matrix of our model
%input lambda, the parameter matrix of our model
%input x, The values to feed to f*
%input n, The length of x
%output y, The vector of length n of f*'s outputs
function y = fPlot(cyc, eta, p, lambda, x, n)
    y = zeros(1,n);
    for i=1:n
        y(1,i) = fDelta(cyc,eta,p,lambda,x(1,i));
    end
end