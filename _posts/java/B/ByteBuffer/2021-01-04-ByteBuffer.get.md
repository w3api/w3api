---
title: ByteBuffer.get()
permalink: Java/ByteBuffer/get
date: 2021-01-04
key: JavaJava.B.ByteBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract byte get()
public ByteBuffer get(byte[] dst)
public ByteBuffer get(byte[] dst, int offset, int length)
public abstract byte get(int index)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **byte[] dst**,  {% include w3api/param_description.html metodo=_data parametro="byte[] dst" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [BufferUnderflowException](/Java/BufferUnderflowException/)

## Clase Padre
[ByteBuffer](/Java/ByteBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.ByteBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
