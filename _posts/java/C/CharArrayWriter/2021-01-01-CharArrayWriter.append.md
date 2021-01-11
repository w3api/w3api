---
title: CharArrayWriter.append()
permalink: Java/CharArrayWriter/append
date: 2021-01-11
key: JavaJava.C.CharArrayWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharArrayWriter.metodos valor="append" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CharArrayWriter append(char c)
public CharArrayWriter append(CharSequence csq)
public CharArrayWriter append(CharSequence csq, int start, int end)
~~~

## Parámetros
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence csq" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}

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
