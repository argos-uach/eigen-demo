# eigen-demo

Para probar este ejemplo se recomienda crear un ambiente conda como sigue

    conda create -n c-eigen -c conda-forge make cmake cxx-compiler eigen

Luego activar el ambiente 

    conda activate c-eigen

Compilar el demo

    make

y ejecutar

    python ejemplo.py

El resultado debería ser 

    2*matriz =
    2 4
    6 8

Desde ejemplo.py entregamos un numpy ndarray a la funcion sumMatrix de demo.cpp como argumento, que retorna una matriz eigen::MatrixXf (es la multiplicación de la matriz entregada como argumento pr 2)

Luego hacemos un test unitario test_demo.py para verificar que la multiplicación sea correcta en python, para probar el testing debemos instalar:

    conda install pip pytest -c conda-forge

Notar que debe instalarse en el ambiente c-eigen