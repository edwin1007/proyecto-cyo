include "alldifferent.mzn";

int: n = 4;
int: m = 2*(n-1);
int: Min = 1;
int: Max = 3;
array[1..n, 1..n] of var int: D = [|  0, 745, 665, 929 |
                                    745,   0,  80, 337 |
                                    665,  80,   0, 380 |
                                    929, 337, 380,   0 |];
array[1..m, 1..n] of var int: s; % solucion
array[1..m, 1..n] of var int: pn; % positivos y negativos
var int: utilidad;

constraint forall(j in 1..m) (alldifferent([abs(s[j, i]) | i in 1..n])); % elementos no repetidos en filas
constraint forall(i in 1..n) (alldifferent([s[j, i] | j in 1..m])); % elementos no repetidos en columnas
constraint forall(i in 1..n, j in 1..m) (abs(s[j, i]) != i); % evita la diagonal de ceros
constraint forall(i in 1..n, j in 2..m) (abs(s[j, i]) != abs(s[j-1, i]));  % se quita la opcion de que se juegue contra si mismo
constraint forall(i in 1..m)(let {var int: positivos = count(j in 1..n)(s[i,j] > 0),
                                  var int: negativos = count(j in 1..n)(s[i,j] < 0)} 
                                  in positivos = negativos); % tener la misma cantidad de positivos y negativos en cada fila
constraint forall(i in 1..m, j in 1..n) (if s[i,j] > 0 then s[i, s[i, j]] = -j endif); % genera los cruces para que un equipo sea visitante y el otro local
constraint forall(i in 1..m, j in 1..n) (pn[i, j] = if s[i, j] > 0 then 0 else 1 endif); % se crea la matrix que identifica donde hay numeros positivos y negativos 
constraint forall(j in 1..n) (forall(i in 1..m-Max) (let {var int: condicion = count(k in 1..Max)(pn[i,j] != pn[i+k,j])} 
                                                     in condicion >= 1)); % maximo de las giras y permanencias
constraint utilidad = sum(i in 1..n) (sum(j in 1..m) (if pn[j, i] == 1 then 
                                                                      if j == 1 then D[abs(s[j, i]), i]
                                                                      else
                                                                           if pn[j-1, i] == 1 then D[abs(s[j, i]), abs(s[j-1, i])]
                                                                           else
                                                                                D[abs(s[j, i]), i]
                                                                           endif
                                                                      endif 
                                                 else 
                                                      if pn[j-1, i] == 1 /\ j > 1 then D[i, abs(s[j-1, i])] 
                                                      else 0 
                                                      endif
                                                 endif + if pn[j, i] == 1 /\ j == m then D[i, abs(s[j, i])] 
                                                         else 0 endif));% funcion objetivo  

                        
%constraint utilidad = sum(i in 1..n, j in 1..m) (c[j,i]);

solve minimize utilidad;