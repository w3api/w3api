---
title: CharBuffer.append()
permalink: Java/CharBuffer/append
date: 2021-01-04
key: JavaJava.C.CharBuffer
category: java
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
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence csq" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CharBuffer](/Java/CharBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
