

A = [[37 67 93]
     [80 84 59]
     [93 58 42]];     

[L, U, P, Q] = lu(A);
product1 = P*A*Q;
product2 = L*U;

fprintf('A:\n');
disp(A);
fprintf('L:\n');
disp(L);
fprintf('U:\n');
disp(U);
fprintf('P:\n');
disp(P);
fprintf('Q:\n');
disp(Q);
fprintf('Product of PAQ:\n');
disp(product1);
fprintf('Product of LU:\n');
disp(product2);

