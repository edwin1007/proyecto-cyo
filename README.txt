
*******************************************************************************************
*********************  INICIO EJECUCION DE PROGRAMA  **************************************
*******************************************************************************************

1. Ejecutar los archivo CalDep.mzn y DatosCalDep.dzn para verificar el funcionameinto
    del codigo y ver las salidas de los calendarios optimos de acuerdo a las 
    restricciones. El codigo funciona con CHUFFED Y GECODE  

2. GUI: debido a los inconvenientes de integrar la GUI con ejecucion de codigo
    en minizinc, no es posible ver los resultados como salida en la interfaz
    grafica.

3. Para ejecutar las demas instancias, se deben cambiar los datos del archivo
    DatosCalDep.dzn por alguna de las instancias incluidas en el archivo 
    otras-instancias.txt, ya que el archivo DatosCalDep.dzn solo reconoce una
    solo entrada. 

4. El archivo salidaCalendarios.txt contiene todas las salidas optimas para la primera instancia.

5. Los demas archivos no nombrados aqui, son las salidas al ejecutar el archivo CalDep.mzn y 
    DatosCalDep.dzn junto con el compilador. 

    ejecucion en windows:

    5.1. Para ejecutar archivo .mzn + archivo .dzn con compilador (chuffed, gecode...):  

    ruta-minizinc.exe + .\minizinc + -c --solver + (compilador) ruta-archivo.mzn + ruta-archivo.dzn 

    C:\Program Files\MiniZinc> .\minizinc -c --solver chuffed 
    Users\'EDWIN ACER'\Desktop\Ejemplo-minizinc\CalDep.mzn  
    \Users\'EDWIN ACER'\Desktop\proyecto-cyo\DatosCalDep.dzn

*******************************************************************************************
************************  FIN EJECUCION DE PROGRAMA  **************************************
*******************************************************************************************


===========================================================================================
===========================================================================================

Seccion solo informativa:

Para ejecutar programa en windows. 

1. /** solo ejecutar archivo.mzn -> sin incluir archivos .dzn*/

ruta-minizinc.exe + .\minizinc + ruta-archivo.mzn

C:\'Program Files'\MiniZinc .\minizinc \Users\'EDWIN ACER'\Desktop\proyecto-cyo\CalDep.mzn

===================================================================
2. Para ejecutar archivo .mzn + archivo .dzn:  

ruta-minizinc.exe + .\minizinc + ruta-archivo.mzn + ruta-archivo.dzn 

C:\Program Files\MiniZinc> .\minizinc \Users\'EDWIN ACER'\Desktop\Ejemplo-minizinc\CalDep.mzn  
\Users\'EDWIN ACER'\Desktop\proyecto-cyo\DatosCalDep.dzn

===================================================================
2. Para ejecutar archivo .mzn + archivo .dzn con compilador (chuffed, gecode...):  

ruta-minizinc.exe + .\minizinc + -c --solver + (compilador) ruta-archivo.mzn + ruta-archivo.dzn 

C:\Program Files\MiniZinc> .\minizinc -c --solver chuffed Users\'EDWIN ACER'\Desktop\Ejemplo-minizinc\CalDep.mzn  
\Users\'EDWIN ACER'\Desktop\proyecto-cyo\DatosCalDep.dzn

===================================================================
3. /** solo para ejecutar archivo.fzn */

PS C:\Program Files\MiniZinc> .\minizinc C:\Users\'EDWIN ACER'\Desktop\Ejemplo-minizinc\CalDep.fzn

===================================================================
4. /** para ejecutar las demas instancias de deben cambiar los datos por los que estan contenidos 
    en el archivo otras-instancias.txt */ 

===========================================================================================
===========================================================================================