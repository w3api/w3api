---
title: FloatBuffer.get()
permalink: Java/FloatBuffer/get
date: 2021-01-04
key: JavaJava.F.FloatBuffer
category: java
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **float[] dst**,  {% include w3api/param_description.html metodo=_data parametro="float[] dst" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [BufferUnderflowException](/Java/BufferUnderflowException/)

## Clase Padre
[FloatBuffer](/Java/FloatBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FloatBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
