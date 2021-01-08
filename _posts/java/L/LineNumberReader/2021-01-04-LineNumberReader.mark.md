---
title: LineNumberReader.mark()
permalink: Java/LineNumberReader/mark
date: 2021-01-04
key: JavaJava.L.LineNumberReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineNumberReader.metodos valor="mark" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void mark(int readAheadLimit) throws IOException
~~~

## Parámetros
* **int readAheadLimit**,  {% include w3api/param_description.html metodo=_data parametro="int readAheadLimit" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[LineNumberReader](/Java/LineNumberReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LineNumberReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
