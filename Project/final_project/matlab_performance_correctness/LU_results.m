A = [[60 37 42]
[49 66 99]
[22 4 31]];



[L,U] = lu(A);
Product = L*U;

fprintf('A:\n');
disp(A);
fprintf('L:\n');
disp(L);
fprintf('U:\n');
disp(U);
fprintf('Product:\n');
disp(Product);