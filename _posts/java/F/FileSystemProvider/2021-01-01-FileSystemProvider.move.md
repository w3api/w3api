---
title: FileSystemProvider.move()
permalink: Java/FileSystemProvider/move
date: 2021-01-11
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="move" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void move(Path source, Path target, CopyOption... options) throws IOException
~~~

## Parámetros
* **CopyOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="CopyOption... options" %}
* **Path target**,  {% include w3api/param_description.html metodo=_dato parametro="Path target" %}
* **Path source**,  {% include w3api/param_description.html metodo=_dato parametro="Path source" %}

## Excepciones
[FileAlreadyExistsException](/Java/FileAlreadyExistsException/), [IOException](/Java/IOException/), [DirectoryNotEmptyException](/Java/DirectoryNotEmptyException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [AtomicMoveNotSupportedException](/Java/AtomicMoveNotSupportedException/)

## Clase Padre
[FileSystemProvider](/Java/FileSystemProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
