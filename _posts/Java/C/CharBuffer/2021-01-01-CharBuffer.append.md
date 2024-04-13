---
title: CharBuffer.append()
permalink: /Java/CharBuffer/append/
date: 2021-01-11
key: Java.C.CharBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharBuffer.metodos valor="append" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CharBuffer append(char c)
public CharBuffer append(CharSequence csq)
public CharBuffer append(CharSequence csq, int start, int end)
~~~

## Parámetros
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence csq" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/)

## Clase Padre
[CharBuffer](/Java/CharBuffer/)

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
