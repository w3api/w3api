---
title: CharArrayReader.read()
permalink: Java/CharArrayReader/read
date: 2021-01-11
key: JavaJava.C.CharArrayReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharArrayReader.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read() throws IOException
public int read(char[] b, int off, int len) throws IOException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **char[] b**,  {% include w3api/param_description.html metodo=_dato parametro="char[] b" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[CharArrayReader](/Java/CharArrayReader/)

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
