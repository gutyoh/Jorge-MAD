El programa MAD (Manejador de Archivos Duplicados) es sencillo, lo que hace es tomar una ruta que se pasa por la linea de comando y el programa buscara los archivos duplicados que esten dentro del mismo.

Para poder usar el programa facilmente esta la carpeta _**root_folder**_, esta contiene una cantidad de archivos "boilerplate" con los que se puede probar el programa.

_____

Como usar en `Python`:
```
$ python main.py root_folder

Enter file format:


Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
1

35 bytes
root_folder\files\some_text.txt
root_folder\info.txt

34 bytes
root_folder\files\stage\src\src.txt
root_folder\files\stage\src\toggleminimenu.js
root_folder\project\extraversion.csv
root_folder\project\index.html
root_folder\project\python_copy.txt
root_folder\python.txt

32 bytes
root_folder\calc\bikeshare.csv
root_folder\calc\server.php
root_folder\files\stage\src\index.js
root_folder\files\stage\src\libs.txt
root_folder\files\stage\src\reviewslider.js
root_folder\files\stage\src\spoiler.js
root_folder\files\stage\cars.json
root_folder\files\stage\package-lock.json
root_folder\files\db_cities.js
root_folder\lost.json
root_folder\phones.csv

Check for duplicates?
yes

35 bytes
Hash: d63a4f1856c5fa167b1aaa6529d9846f
1. root_folder\files\some_text.txt
2. root_folder\info.txt
34 bytes
Hash: a5ceea9b58986bc87fb85f999d76d9db
3. root_folder\project\python_copy.txt
4. root_folder\python.txt
32 bytes
Hash: c2a5ad1655d8d46d7d699594c1ee0dec
5. root_folder\calc\bikeshare.csv
6. root_folder\phones.csv
Hash: 95708df6eb2d9e30c128cf14dcf91f5b
7. root_folder\files\stage\cars.json
8. root_folder\lost.json

Delete files?
yes

Enter file numbers to delete:
1 9 7 

Wrong format # Muestra error porque el archivo '9' no existe!

Enter file numbers to delete:
1 2 4

Total freed up space: 104 bytes
```

TOMAR EN CUENTA que para revisar TODOS los archivos no es necesario escribir nada en el diálogo de `Enter file format:` en este punto simplemente lo dejamos vacío, apretamos `ENTER` directo que sería el equivalente a un `\n` y asi podremos ver todos los archivos en el directorio.

______

En caso que querramos revisar archivos con extensión ESPECIFICA solo debemos pasar la extensíon sin el `.` punto por delante:

```
# Para revisar TODOS LOS ARCHIVOS en el directorio:

Enter file format:
  # dejar vacio! solamente apretar ENTER en este punto, equivalente a '\n'
...

# Para revisar csv:

Enter file format:
csv

...

# Para revisar txt:

Enter file format:
txt

...
```
______

Por último el uso en `Go` es identico a `Python`, lo unico que cambia es la manera de ejecutarlo pues debemos correr `go run main.go root_folder`:
```
$ go run main.go root_folder

// seguir mismos pasos que en el ejemplo de uso en Python
```
