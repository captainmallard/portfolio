%   Coin flip simulation with M coins!
%   AUTHOR: Philip de Castro, 2017

tic
N = 100000; %number of runs
num_coins = 100; %number of coins
flipped_coins = randi(2,N,num_coins); %produce the flipped coins
Heads = flipped_coins == 1; %create a matrix of 1 and 0
vec_heads = sum(Heads,2); %sum up each row and create a vector
total_heads = sum(vec_heads);

ph = zeros(100, 1); %define vector of 100 rows for probability of heads
for num_heads = 1:100 %for-loop
     ph(num_heads) = sum(vec_heads == num_heads)/N; %total number of a number of heads divided by the total run.
end
plot(ph, 'm') %plot it in Pascal Purple!
title('Probability Distribution of Coin Flips')
toc









