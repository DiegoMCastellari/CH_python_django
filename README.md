# CH_python_django     
CoderHouse Python-Django course     

# Inicio     
Header con NavBar para navegar por las distintas pagínas.     
Se puede ingresar a cada página para ver los datos presentes en cada tabla o ingresar a cada formulario para agregar datos.    

# Páginas de datos    
Existe un página para cada una de las tablas (jugadores, equipos y ligas), donde se muestran los datos que cada una de estas.     
Además, cuenta con un buscador, para buscar por coincidencia de strings. Para realizar una búsqueda, ingresar un texto y clickear el botón de Buscar. Existen tres posibles resultados:     
- en caso de encontrar una coincidencia, mostrará en un texto la búsqueda realizada y el resultado de la misma en la tabla;    
- en caso de no encontrar una coincidencia, mostrará el texto en color "Ningún objeto cumple con el filtro!";    
- en caso de no ingresar nada a la búsqueda, mostrará en color el texto "Filtro no ingresado!".    
Finalmente, debajo de la tabla, se encontrará un botón para ingresar al formulario de ese modelo.

# Páginas de formularios
Existe una página de formulario para cada uno de los modelos (jugadores, equipos y ligas).    
Para cargar un registro, ingresar los datos correspondientes y clickear Agregar. Las fechas se deben ingresar con el formato 2023-01-01.      
Luego de agregar un nuevo registro, se redireccionará a la página de ese modelo, a la sección de la tabla, donde estará el registro agregado.