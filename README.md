# eigen-demo

Para probar este ejemplo se recomienda crear un ambiente conda como sigue

    conda create -n c-eigen -c conda-forge make cmake cxx-compiler eigen

Luego activar el ambiente 

    conda activate c-eigen

Compilar el demo

    make

y ejecutar

    ./demo

El resultado debería ser 

    a + b =
    3 5
    4 8
    a - b =
    -1 -1
    2  0
    Doing a += b;
    Now a =
    3 5
    4 8
    -v + w - v =
    -1
    -4
    -6