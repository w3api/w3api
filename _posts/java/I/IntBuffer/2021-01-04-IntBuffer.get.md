---
title: IntBuffer.get()
permalink: Java/IntBuffer/get
date: 2021-01-04
key: JavaJava.I.IntBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int get()
public abstract int get(int index)
public IntBuffer get(int[] dst)
public IntBuffer get(int[] dst, int offset, int length)
~~~

## Parámetros
* **int[] dst**,  {% include w3api/param_description.html metodo=_data parametro="int[] dst" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [BufferUnderflowException](/Java/BufferUnderflowException/)

## Clase Padre
[IntBuffer](/Java/IntBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
