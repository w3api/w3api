---
title: DoubleBuffer.put()
permalink: /Java/DoubleBuffer/put/
date: 2021-01-11
key: Java.D.DoubleBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DoubleBuffer put(double d)
public final DoubleBuffer put(double[] src)
public DoubleBuffer put(double[] src, int offset, int length)
public abstract DoubleBuffer put(int index, double d)
public DoubleBuffer put(DoubleBuffer src)
~~~

## Parámetros
* **double d**,  {% include w3api/param_description.html metodo=_dato parametro="double d" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **DoubleBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleBuffer src" %}
* **double[] src**,  {% include w3api/param_description.html metodo=_dato parametro="double[] src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DoubleBuffer](/Java/DoubleBuffer/)

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
