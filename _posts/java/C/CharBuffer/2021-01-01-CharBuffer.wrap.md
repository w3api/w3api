---
title: CharBuffer.wrap()
permalink: Java/CharBuffer/wrap
date: 2021-01-11
key: JavaJava.C.CharBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharBuffer.metodos valor="wrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CharBuffer wrap(char[] array)
public static CharBuffer wrap(char[] array, int offset, int length)
public static CharBuffer wrap(CharSequence csq)
public static CharBuffer wrap(CharSequence csq, int start, int end)
~~~

## Parámetros
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence csq" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **char[] array**,  {% include w3api/param_description.html metodo=_dato parametro="char[] array" %}
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CharBuffer](/Java/CharBuffer/)

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
