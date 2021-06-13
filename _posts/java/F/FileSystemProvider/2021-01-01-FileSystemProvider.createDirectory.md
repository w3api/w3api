---
title: FileSystemProvider.createDirectory()
permalink: /Java/FileSystemProvider/createDirectory/
date: 2021-01-11
key: Java.F.FileSystemProvider
category: Java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="createDirectory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void createDirectory(Path dir, FileAttribute<?>... attrs) throws IOException
~~~

## Parámetros
* **Path dir**,  {% include w3api/param_description.html metodo=_dato parametro="Path dir" %}
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_dato parametro="FileAttribute<?>... attrs" %}

## Excepciones
[IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [FileAlreadyExistsException](/Java/FileAlreadyExistsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
