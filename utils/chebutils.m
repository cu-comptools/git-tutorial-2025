function [D, x] = cheb(n)
%
% Hint: https://people.maths.ox.ac.uk/trefethen/book.pdf, Chapter 6, pages
% 51-55.
% Without arguments, this function should do a self-check.
%
if nargin==0, test_cheb; return; end

if n==0
    x = 1;
    D = 0;
else
    x = cos(pi*(0:n)/n)';
    c = [2; ones(n-1, 1); 2].*(-1).^(0:n)';
    x = repmat(x, 1, n+1);
    dx = x - x';
    D = (c*(1./c)')./(dx + (eye(n+1)));
    D = D - diag(sum(D'));
end

%%%
function test_cheb
