---
title: CharArrayWriter.writeTo()
permalink: /Java/CharArrayWriter/writeTo/
date: 2021-01-11
key: Java.C.CharArrayWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharArrayWriter.metodos valor="writeTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeTo(Writer out) throws IOException
~~~

## Parámetros
* **Writer out**,  {% include w3api/param_description.html metodo=_dato parametro="Writer out" %}

## Excepciones
[IOException](/Java/IOException/)

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
