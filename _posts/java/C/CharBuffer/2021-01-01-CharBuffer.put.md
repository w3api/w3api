---
title: CharBuffer.put()
permalink: Java/CharBuffer/put
date: 2021-01-11
key: JavaJava.C.CharBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CharBuffer put(char c)
public final CharBuffer put(char[] src)
public CharBuffer put(char[] src, int offset, int length)
public abstract CharBuffer put(int index, char c)
public final CharBuffer put(String src)
public CharBuffer put(String src, int start, int end)
public CharBuffer put(CharBuffer src)
~~~

## Parámetros
* **CharBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="CharBuffer src" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **String src**,  {% include w3api/param_description.html metodo=_dato parametro="String src" %}
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **char[] src**,  {% include w3api/param_description.html metodo=_dato parametro="char[] src" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
