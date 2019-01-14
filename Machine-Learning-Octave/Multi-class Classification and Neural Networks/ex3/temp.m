

num_labels = 10;          % 10 labels, from 1 to 10
                          % (note that we have mapped "0" to label 10)

%% =========== Part 1: Loading and Visualizing Data =============
%  We start the exercise by first loading and visualizing the dataset.
%  You will be working with a dataset that contains handwritten digits.
%


load('ex3data1.mat'); % training data stored in arrays X, y

size(X)
size(y)
lambda = 0.1
[all_theta] = oneVsAll(X, y, num_labels, lambda)


%% ================ Part 3: Predict for One-Vs-All ================



m = size(X, 1)
num_labels = size(all_theta, 1)

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1)

% Add ones to the X data matrix
X = [ones(m, 1) X]





