function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%


function[val]=h(theta,xi)
val=xi*theta;
end

for i=1:m
J=J+(h(theta,X(i,:))-y(i))^2;
end

reg=0;
for i=2:size(theta)
reg=reg+theta(i)^2;
end
reg=reg*lambda;

J=(J+reg)/(2*m);

gradtemp=grad;
for j=1:size(theta)
for i=1:m
gradtemp(j)=gradtemp(j)+(h(theta,X(i,:))-y(i))*X(i,j);
end
if j~=1
gradtemp(j)=gradtemp(j)+(lambda*theta(j));
end
end
grad=gradtemp/m;


% =========================================================================

grad = grad(:);

end
