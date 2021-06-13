---
title: PipedInputStream.PipedInputStream()
permalink: /Java/PipedInputStream/PipedInputStream/
date: 2021-01-11
key: Java.P.PipedInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedInputStream.constructores valor="PipedInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PipedInputStream()
public PipedInputStream(int pipeSize)
public PipedInputStream(PipedOutputStream src) throws IOException
public PipedInputStream(PipedOutputStream src, int pipeSize) throws IOException
~~~

## Parámetros
* **PipedOutputStream src**,  {% include w3api/param_description.html metodo=_dato parametro="PipedOutputStream src" %}
* **int pipeSize**,  {% include w3api/param_description.html metodo=_dato parametro="int pipeSize" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[PipedInputStream](/Java/PipedInputStream/)

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
