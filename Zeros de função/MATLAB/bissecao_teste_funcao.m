epsilon = 1e-10;
a = 5;
b = 0;


m= fi(a,b);
y = f(m);

n = 1;

while abs(y) > epsilon
    if f(a) * y < 0
        b = m;
    else 
        a = m;
    end

    n = n + 1;
    m = fi(a,b);
    y = f(m);
end

fprintf('\n');
fprintf('Valor da raiz:  %.10d \n', m);
fprintf('Erro admitido:  %.2d \n', epsilon);
fprintf('Número de iterações:  %d \n\n', n);

function funcao = f(x)
    funcao = sin(x);
end

function mediap = fi(a,b)
    mediap = (a+b)/2;
end
