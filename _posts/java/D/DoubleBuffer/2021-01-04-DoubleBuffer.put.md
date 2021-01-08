---
title: DoubleBuffer.put()
permalink: Java/DoubleBuffer/put
date: 2021-01-04
key: JavaJava.D.DoubleBuffer
category: java
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
* **DoubleBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="DoubleBuffer src" %}
* **double d**,  {% include w3api/param_description.html metodo=_data parametro="double d" %}
* **double[] src**,  {% include w3api/param_description.html metodo=_data parametro="double[] src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DoubleBuffer](/Java/DoubleBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DoubleBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
