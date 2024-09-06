k = 1;
l = 1;
m = 1;
a = l + 1/2;
c = Sqrt[(2 l + 1)/(2  Pi)  (Factorial[l - m])/(Factorial[l + m])];
s = Simplify[c  LaguerreL[k, a , r^2] r^l*LegendreP[l, Abs[m], Cos[t]] Cos[m  p] , Assumptions -> Sin[t] > 0] 
