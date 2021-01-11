---
title: FileVisitor.visitFile()
permalink: Java/FileVisitor/visitFile
date: 2021-01-11
key: JavaJava.F.FileVisitor
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileVisitor.metodos valor="visitFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileVisitResult visitFile(T file, BasicFileAttributes attrs) throws IOException
~~~

## Parámetros
* **T file**,  {% include w3api/param_description.html metodo=_dato parametro="T file" %}
* **BasicFileAttributes attrs**,  {% include w3api/param_description.html metodo=_dato parametro="BasicFileAttributes attrs" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileVisitor](/Java/FileVisitor/)

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
