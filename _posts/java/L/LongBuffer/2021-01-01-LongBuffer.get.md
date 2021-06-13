---
title: LongBuffer.get()
permalink: /Java/LongBuffer/get/
date: 2021-01-11
key: Java.L.LongBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract long get()
public abstract long get(int index)
public LongBuffer get(long[] dst)
public LongBuffer get(long[] dst, int offset, int length)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **long[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="long[] dst" %}

## Excepciones
[BufferUnderflowException](/Java/BufferUnderflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[LongBuffer](/Java/LongBuffer/)

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
