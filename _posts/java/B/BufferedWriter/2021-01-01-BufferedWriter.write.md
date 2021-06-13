---
title: BufferedWriter.write()
permalink: /Java/BufferedWriter/write/
date: 2021-01-11
key: Java.B.BufferedWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(char[] cbuf, int off, int len) throws IOException
public void write(int c) throws IOException
public void write(String s, int off, int len) throws IOException
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **int c**,  {% include w3api/param_description.html metodo=_dato parametro="int c" %}
* **char[] cbuf**,  {% include w3api/param_description.html metodo=_dato parametro="char[] cbuf" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[BufferedWriter](/Java/BufferedWriter/)

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
