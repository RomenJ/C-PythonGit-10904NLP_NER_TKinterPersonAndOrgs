Analizador NER para la Identificación de Personas y Organizaciones en Textos en Inglés
Este proyecto consiste en una herramienta de análisis de texto diseñada para identificar entidades nombradas (NER, por sus siglas en inglés) en textos en inglés, específicamente personas y organizaciones. El programa utiliza el modelo de lenguaje natural en inglés de la biblioteca Spacy para llevar a cabo esta tarea. Además, cuenta con una interfaz gráfica simple desarrollada con la biblioteca Tkinter de Python, lo que facilita su uso para usuarios con diversos niveles de habilidad técnica.

Características
Carga de Archivos: Los usuarios pueden cargar archivos de texto en inglés (.txt) utilizando un explorador de archivos integrado en la interfaz de usuario.
Análisis de Texto: Una vez que se carga el archivo de texto, los usuarios pueden iniciar el análisis de texto con un clic de botón. El programa identificará automáticamente las personas y organizaciones mencionadas en el texto.
Búsqueda de Coincidencias: Los usuarios tienen la opción de especificar un objetivo de búsqueda, ya sea una persona o una organización, y el programa buscará coincidencias exactas en el texto.
Contexto de Coincidencias: Para cada coincidencia encontrada, el programa proporciona un contexto, mostrando parte del texto que rodea la entidad nombrada encontrada, lo que ayuda a comprender mejor su contexto dentro del documento.
Resultados Detallados: Al finalizar el análisis, se muestran los resultados en una ventana emergente que incluye el número total de coincidencias encontradas tanto para personas como para organizaciones.
Instalación
Para utilizar este programa, se recomienda tener instalado Python 3 y las bibliotecas necesarias. Puede instalar las dependencias utilizando el siguiente comando:

bash
Copy code
pip install -r requirements.txt
Una vez instaladas las dependencias, simplemente ejecute el archivo main.py para iniciar la aplicación.

Contribuciones
Las contribuciones son bienvenidas. Si desea contribuir a este proyecto, puede bifurcar el repositorio y enviar una solicitud de extracción con sus mejoras propuestas.

Problemas y Sugerencias
Si encuentra algún problema o tiene alguna sugerencia de mejora, no dude en abrir un problema en el repositorio de GitHub.

Licencia
Este proyecto está bajo la licencia MIT. Puede consultar el archivo LICENSE para obtener más información.

Créditos
Este proyecto fue creado por Romen J. powered by Open AI
