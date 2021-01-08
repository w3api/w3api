---
title: OutputStreamWriter.write()
permalink: Java/OutputStreamWriter/write
date: 2021-01-04
key: JavaJava.O.OutputStreamWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OutputStreamWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(char[] cbuf, int off, int len) throws IOException
public void write(int c) throws IOException
public void write(String str, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int c**,  {% include w3api/param_description.html metodo=_data parametro="int c" %}
* **char[] cbuf**,  {% include w3api/param_description.html metodo=_data parametro="char[] cbuf" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[OutputStreamWriter](/Java/OutputStreamWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OutputStreamWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
