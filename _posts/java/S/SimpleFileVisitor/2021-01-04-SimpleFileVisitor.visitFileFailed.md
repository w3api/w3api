---
title: SimpleFileVisitor.visitFileFailed()
permalink: Java/SimpleFileVisitor/visitFileFailed
date: 2021-01-04
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
* **IOException exc**,  {% include w3api/param_description.html metodo=_data parametro="IOException exc" %}
* **T file**,  {% include w3api/param_description.html metodo=_data parametro="T file" %}

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
{%- for _ldc in site.data.Java.S.SimpleFileVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
