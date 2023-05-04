# Analizador sintáctico de Gramáticas libres de contexto.
<br>Ingeneria en desarrollo de software<br>
Programación de sistemas
<br>Brandon Alan Rodríguez Ramírez
<br>./AnalizadorSintactico
<br>Gramatica:<br>
E-> E+T|T<br>
T-> T*F\F<br>
F-> (E)|i<br>

Gramatica sin recursividad:<br>
E-> TFE'<br>
E'-> +TE'|ε<br>
T-> FT'<br>
T'-> *FT'|ε<br>
F-> (E)|i<br>
