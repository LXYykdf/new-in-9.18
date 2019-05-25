delta_3 = a3 - yk';
delta_2 = (Theta2' * delta_3) .* sigmoidGradient(z_2);
delta_2 = delta_2(2:end,:);
Theta1_grad = delta_2 * a1';
Theta2_grad = delta_3 * a2';

Theta1_grad(:,2:end)=Theta1_grad(:,2:end)+lambda* Theta1(:,2:end);
Theta1_grad = Theta1_grad./m;
Theta2_grad(:,2:end)=Theta2_grad(:,2:end)+lambda* Theta2(:,2:end);
Theta2_grad = Theta2_grad./m;
