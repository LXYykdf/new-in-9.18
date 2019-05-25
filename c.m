a1 = [ones(1,m);X'];
z_2 = Theta1 * a1;
a2 = [ones(1,m) ; sigmoid(z_2)];
z_2 = [ones(1,m);z_2];
z_3 = Theta2 * a2;
a3 = sigmoid(z_3); 
h = a3';
yk= 1:num_labels==y;
J = -1/m * sum(sum(yk.*log(h)+(1-yk).*log(1-h))) + ...
lambda / (2*m)*(sum(sum(Theta1(:,2:end).*Theta1(:,2:end)))+ ...
sum(sum(Theta2(:,2:end).*Theta2(:,2:end))));
