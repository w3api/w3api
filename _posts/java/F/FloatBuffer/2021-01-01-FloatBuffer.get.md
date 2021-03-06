---
title: FloatBuffer.get()
permalink: /Java/FloatBuffer/get/
date: 2021-01-11
key: Java.F.FloatBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FloatBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract float get()
public FloatBuffer get(float[] dst)
public FloatBuffer get(float[] dst, int offset, int length)
public abstract float get(int index)
~~~

## Parámetros
* **float[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="float[] dst" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BufferUnderflowException](/Java/BufferUnderflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[FloatBuffer](/Java/FloatBuffer/)

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
