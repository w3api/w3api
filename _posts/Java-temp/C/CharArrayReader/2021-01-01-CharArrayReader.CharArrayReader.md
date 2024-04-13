---
title: CharArrayReader.CharArrayReader()
permalink: /Java/CharArrayReader/CharArrayReader/
date: 2021-01-11
key: Java.C.CharArrayReader
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharArrayReader.constructores valor="CharArrayReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CharArrayReader(char[] buf)
public CharArrayReader(char[] buf, int offset, int length)
~~~

## Parámetros
* **char[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="char[] buf" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CharArrayReader](/Java/CharArrayReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
