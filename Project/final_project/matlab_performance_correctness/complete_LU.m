tic;

A = [[77 61 99]
 [51 22 54]
 [ 6 90 42]];
 
B = [[77 61 99]
 [51 22 54]
 [ 6 90 42]];
 
C = [[4 5 88]
 [97 6 81]
 [93 90 68]];
 
D = [[90 78 86]
 [61 15 39]
 [2 33 92]];
 
E = [[29 86 50]
 [72 53 9]
 [47 59 50]];
 
F = [[91 72 57]
 [94 71 83]
 [59 78 86]];
 
G = [[75 50 9]
 [49 86 63]
 [85 80 60]];
 
H = [[6 16 69]
 [6 17 20]
 [83 91 43]];
 
I = [[41 75 80]
 [46 8 3]
 [28 15 13]];
 
J = [[33 28 17]
 [63 1 12]
 [80 18 9]];
for index= [ 1:1 ]
[L1 U1 p1 q1] = lucp(A);
[L2 U2 p2 q2] = lucp(B);
[L3 U3 p3 q3] = lucp(C);
[L4 U4 p4 q4] = lucp(D);
[L5 U5 p5 q5] = lucp(E);
[L6 U6 p6 q6] = lucp(F);
[L7 U7 p7 q7] = lucp(G);
[L8 U8 p8 q8] = lucp(H);
[L9 U9 p9 q9] = lucp(I);
[L10 U10 p10 q10] = lucp(J);
end

wtime = toc;
fprintf ( 1, '  MY_PROGRAM took %f seconds to run.\n', wtime );