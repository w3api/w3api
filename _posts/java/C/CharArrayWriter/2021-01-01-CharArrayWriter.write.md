---
title: CharArrayWriter.write()
permalink: /Java/CharArrayWriter/write/
date: 2021-01-11
key: Java.C.CharArrayWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharArrayWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(char[] c, int off, int len)
public void write(int c)
public void write(String str, int off, int len)
~~~

## Parámetros
* **int c**,  {% include w3api/param_description.html metodo=_dato parametro="int c" %}
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **char[] c**,  {% include w3api/param_description.html metodo=_dato parametro="char[] c" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CharArrayWriter](/Java/CharArrayWriter/)

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
