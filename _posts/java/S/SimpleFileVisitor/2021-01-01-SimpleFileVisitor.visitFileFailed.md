---
title: SimpleFileVisitor.visitFileFailed()
permalink: Java/SimpleFileVisitor/visitFileFailed
date: 2021-01-11
key: JavaJava.S.SimpleFileVisitor
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleFileVisitor.metodos valor="visitFileFailed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileVisitResult visitFileFailed(T file, IOException exc) throws IOException
~~~

## Parámetros
* **T file**,  {% include w3api/param_description.html metodo=_dato parametro="T file" %}
* **IOException exc**,  {% include w3api/param_description.html metodo=_dato parametro="IOException exc" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[SimpleFileVisitor](/Java/SimpleFileVisitor/)

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
