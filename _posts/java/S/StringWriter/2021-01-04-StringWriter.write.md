---
title: StringWriter.write()
permalink: Java/StringWriter/write
date: 2021-01-04
key: JavaJava.S.StringWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(char[] cbuf, int off, int len)
public void write(int c)
public void write(String str)
public void write(String str, int off, int len)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int c**,  {% include w3api/param_description.html metodo=_data parametro="int c" %}
* **char[] cbuf**,  {% include w3api/param_description.html metodo=_data parametro="char[] cbuf" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[StringWriter](/Java/StringWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
