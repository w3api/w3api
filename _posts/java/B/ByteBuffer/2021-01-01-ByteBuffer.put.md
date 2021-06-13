---
title: ByteBuffer.put()
permalink: /Java/ByteBuffer/put/
date: 2021-01-11
key: JavaJava.B.ByteBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ByteBuffer put(byte b)
public final ByteBuffer put(byte[] src)
public ByteBuffer put(byte[] src, int offset, int length)
public abstract ByteBuffer put(int index, byte b)
public ByteBuffer put(ByteBuffer src)
~~~

## Parámetros
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}
* **byte[] src**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] src" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **byte b**,  {% include w3api/param_description.html metodo=_dato parametro="byte b" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ByteBuffer](/Java/ByteBuffer/)

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
