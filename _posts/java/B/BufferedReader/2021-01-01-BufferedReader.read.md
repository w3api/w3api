---
title: BufferedReader.read()
permalink: /Java/BufferedReader/read/
date: 2021-01-11
key: JavaJava.B.BufferedReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedReader.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read() throws IOException
public int read(char[] cbuf, int off, int len) throws IOException
~~~

## Parámetros
* **char[] cbuf**,  {% include w3api/param_description.html metodo=_dato parametro="char[] cbuf" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[BufferedReader](/Java/BufferedReader/)

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
