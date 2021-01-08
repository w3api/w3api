---
title: PipedReader.PipedReader()
permalink: Java/PipedReader/PipedReader
date: 2021-01-04
key: JavaJava.P.PipedReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedReader.constructores valor="PipedReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PipedReader()
public PipedReader(int pipeSize)
public PipedReader(PipedWriter src) throws IOException
public PipedReader(PipedWriter src, int pipeSize) throws IOException
~~~

## Parámetros
* **int pipeSize**,  {% include w3api/param_description.html metodo=_data parametro="int pipeSize" %}
* **PipedWriter src**,  {% include w3api/param_description.html metodo=_data parametro="PipedWriter src" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PipedReader](/Java/PipedReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PipedReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
