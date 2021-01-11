---
title: IntBuffer.put()
permalink: Java/IntBuffer/put
date: 2021-01-11
key: JavaJava.I.IntBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract IntBuffer put(int i)
public final IntBuffer put(int[] src)
public IntBuffer put(int[] src, int offset, int length)
public abstract IntBuffer put(int index, int i)
public IntBuffer put(IntBuffer src)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int[] src**,  {% include w3api/param_description.html metodo=_dato parametro="int[] src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **IntBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="IntBuffer src" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IntBuffer](/Java/IntBuffer/)

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
