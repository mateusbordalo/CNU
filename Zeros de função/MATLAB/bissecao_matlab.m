epsilon = 1e-10;
a = 4;
b = 0;


m= (a+b)/2;
y = sin(m);

n = 1;
valores_parciais = [m];

while abs(y) > epsilon
    if sin(a) * y < 0
        b = m;
    else 
        a = m;
    end

    n = n + 1;
    m = (a + b) / 2;
    y = sin(m);
end

disp(m);
fprintf('Valor da raiz:%.10d \n', m);
fprintf('Erro admitido:%.2d \n', epsilon);
fprintf('Número de iterações:%d \n', n);

