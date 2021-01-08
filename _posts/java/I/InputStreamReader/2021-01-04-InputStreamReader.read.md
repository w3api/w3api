---
title: InputStreamReader.read()
permalink: Java/InputStreamReader/read
date: 2021-01-04
key: JavaJava.I.InputStreamReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputStreamReader.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read() throws IOException
public int read(char[] cbuf, int offset, int length) throws IOException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **char[] cbuf**,  {% include w3api/param_description.html metodo=_data parametro="char[] cbuf" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[InputStreamReader](/Java/InputStreamReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputStreamReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
