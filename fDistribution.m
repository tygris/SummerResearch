%The goal of this file is to test the distribution of f(Delta)
%This file is designed for the Basic Model

%requires deltaFind.m

L_cycle = [0,50,25,225];
p = 0.3;
lambda = 0.3*12/1100;
eta = [1,2;3,4];

%Turn those values into matrices with zeros on the diagonal
P=zeros(4,4);
P = P+p;
P(1:5:16)=0;
Lambda=zeros(4,4);
Lambda=Lambda+lambda;
Lambda(1:5:16)=0;

%find our bounds for the cycle
Delta = deltaFind(L_cycle);

%get the vectors that we want to plot ready
n = 200; %the number of points to plot
x = linspace(Delta(1), Delta(2), n);
display('Here are the values of f( Delta ):')
display('The first value is f( Delta_low ), the last value is f( Delta_up ), and the ')
display('rest are other possible values of f( Delta ) in the range (Delta_low, Delta_up)')
y = fPlot(L_cycle, eta, P, Lambda,x,n) 

%make the diagram of f(Delta) Delta in [Delta_low, Delta_up]
figure(1)
hold on
semilogy(x(1,1),y(1,1),'o',x(1,2:n-1), y(1,2:n-1),x(1,n), y(1,n),'o')
ylabel('Value of f(Delta)')
xlabel('Value of Delta')
axis([0,Delta(2),0,y(1,1)])

