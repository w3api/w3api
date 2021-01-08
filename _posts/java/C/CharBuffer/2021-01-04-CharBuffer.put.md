---
title: CharBuffer.put()
permalink: Java/CharBuffer/put
date: 2021-01-04
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
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **CharBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="CharBuffer src" %}
* **char[] src**,  {% include w3api/param_description.html metodo=_data parametro="char[] src" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **String src**,  {% include w3api/param_description.html metodo=_data parametro="String src" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
