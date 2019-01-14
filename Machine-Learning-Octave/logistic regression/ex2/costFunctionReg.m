function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta



function[val]=costfunc(x,y,theta)
hx=1/(1+inv(e^(x*theta)));
val=-y*log(hx)-(1-y)*log(1-hx);
end;


cost=0;

for i=1:m
cost=cost+costfunc(X(i,:),y(i),theta);
end;
sumedtheta=(theta.^2);
sumedtheta(1,1)=0;
J=(cost/m)+((lambda/(2*m))*sum(sumedtheta));

for j=1:size(theta)
for i=1:m
hx=1/(1+inv(e^(X(i,:)*theta)));
grad(j)=grad(j)+(hx-y(i))*X(i,j);
end;
if (j>1)
grad(j)=grad(j)+lambda*theta(j);
end;
end;
grad=grad/m;







% =============================================================

end
