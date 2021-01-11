---
title: ShortBuffer.put()
permalink: Java/ShortBuffer/put
date: 2021-01-11
key: JavaJava.S.ShortBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ShortBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ShortBuffer put(int index, short s)
public abstract ShortBuffer put(short s)
public final ShortBuffer put(short[] src)
public ShortBuffer put(short[] src, int offset, int length)
public ShortBuffer put(ShortBuffer src)
~~~

## Parámetros
* **short s**,  {% include w3api/param_description.html metodo=_dato parametro="short s" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **short[] src**,  {% include w3api/param_description.html metodo=_dato parametro="short[] src" %}
* **ShortBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ShortBuffer src" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ShortBuffer](/Java/ShortBuffer/)

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
