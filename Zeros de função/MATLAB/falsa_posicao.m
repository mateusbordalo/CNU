epsilon = 1e-5;
a = 4;
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

disp(m);
fprintf('Valor da raiz:%.10d \n', m);
fprintf('Erro admitido:%.2d \n', epsilon);
fprintf('Número de iterações:%d \n', n);

function funcao = f(x)
    funcao = sin(x);
end

function mediap = fi(a,b)
    mediap = (b * abs(f(a)) + abs(f(b)) * a)/(abs(f(a)) + abs(f(b)));
end
