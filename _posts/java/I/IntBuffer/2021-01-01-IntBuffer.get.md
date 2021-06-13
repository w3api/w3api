---
title: IntBuffer.get()
permalink: /Java/IntBuffer/get/
date: 2021-01-11
key: Java.I.IntBuffer
category: Java
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
* **int[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="int[] dst" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BufferUnderflowException](/Java/BufferUnderflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
