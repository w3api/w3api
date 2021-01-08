---
title: DoubleBuffer.get()
permalink: Java/DoubleBuffer/get
date: 2021-01-04
key: JavaJava.D.DoubleBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract double get()
public DoubleBuffer get(double[] dst)
public DoubleBuffer get(double[] dst, int offset, int length)
public abstract double get(int index)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **double[] dst**,  {% include w3api/param_description.html metodo=_data parametro="double[] dst" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [BufferUnderflowException](/Java/BufferUnderflowException/)

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
