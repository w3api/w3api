---
title: FileSystemProvider.newDirectoryStream()
permalink: Java/FileSystemProvider/newDirectoryStream
date: 2021-01-11
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newDirectoryStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DirectoryStream<Path> newDirectoryStream(Path dir, DirectoryStream.Filter<? super Path> filter) throws IOException
~~~

## Parámetros
* **Path dir**,  {% include w3api/param_description.html metodo=_dato parametro="Path dir" %}
* **DirectoryStream.Filter&lt;? super Path&gt; filter**,  {% include w3api/param_description.html metodo=_dato parametro="DirectoryStream.Filter<? super Path> filter" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NotDirectoryException](/Java/NotDirectoryException/), [IOException](/Java/IOException/)

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
