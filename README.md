El programa es sencillo, lo que hace es tomar una ruta que se pasa por la linea de comando y el programa buscara los archivos duplicados que esten dentro del mismo.

Para poder usar el programa facilmente esta la carpeta _**root_folder**_, esta contiene una cantidad de archivos "boilerplate" con los que se puede probar el programa.

_____

Como usar en `Python`:
```
$ python main.py root_folder

Enter file format:
>

Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
> 1

5550640 bytes
root_folder/poker_face.mp3
root_folder/poker_face_copy.mp3

4590560 bytes
root_folder/gordon_ramsay_chicken_breast.avi
root_folder/audio/sia_snowman.mp3
root_folder/audio/rock/smells_like_teen_spirit.mp3

3422208 bytes
root_folder/audio/classic/unknown.mp3
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

Check for duplicates?
> yes

5550640 bytes
Hash: 909ba4ad2bda46b10aac3c5b7f01abd5
1. root_folder/poker_face.mp3
2. root_folder/poker_face_copy.mp3

3422208 bytes
Hash: a7f5f35426b927411fc9231b56382173
3. root_folder/audio/classic/unknown.mp3
4. root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

Delete files?
> yes

Enter file numbers to delete:
> 1 2 5

Wrong format

Enter file numbers to delete:
> 1 2 4

Total freed up space: 14523488 bytes
```

TOMAR EN CUENTA que para revisar TODOS los archivos no es necesario escribir nada en el diálogo de `Enter file format:` en este punto simplemente lo dejamos vacío, apretamos `ENTER` directo que sería el equivalente a un `\n` y asi podremos ver todos los archivos en el directorio.

______

En caso que querramos revisar archivos con extensión ESPECIFICA solo debemos pasar la extensíon sin el `.` punto por delante:

```
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