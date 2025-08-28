function [x1, x2] = quadroots(a, b, c)
% Calculates the roots of the quadratic equation 0 = a*x^2 + b*x + c, and
% returns them as a tuple. If a root is repeated, the elements of the tuple
% will be identical. 
% If called without arguments, the function performs a self-test.
% 
% Parameters
% ----------
% a: float
%     Coefficient of x^2 in the input equation.
%  b: float
%     Coefficient of x in the input equation.
%  c: float
%     Constant coefficient of in the input equation.
% 
%  Returns
%  -------
%  x1, x2: float
%     Roots of the equation.
if nargin==0, test_quadroots; return; end

x1 = (-b + sqrt(b*b - 4*a*c))/2*a;
x2 = (-b - sqrt(b*b - 4*a*c))/2*a;

%%%
function test_quadroots
a = 2;
b = -5;
c = 2;
[root1, root2] = quadroots(a, b, c);
root1exact = 2;
root2exact = 0.5;
assert(abs(root1exact - root1) < 1e-14 && abs(root2exact - root2) < 1e-14);