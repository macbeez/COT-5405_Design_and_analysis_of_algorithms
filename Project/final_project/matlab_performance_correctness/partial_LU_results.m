A = [[92 44 50]
     [59 5 94]
     [94 4 83]];

[L, U, P] = lu(A);
product1 = P*A;
product2 = L*U;

fprintf('A:\n');
disp(A);
fprintf('L:\n');
disp(L);
fprintf('U:\n');
disp(U);
fprintf('P:\n');
disp(P);
fprintf('Product of PA:\n');
disp(product1);
fprintf('Product of LU:\n');
disp(product2);