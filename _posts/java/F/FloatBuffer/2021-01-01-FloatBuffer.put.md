---
title: FloatBuffer.put()
permalink: Java/FloatBuffer/put
date: 2021-01-11
key: JavaJava.F.FloatBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FloatBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract FloatBuffer put(float f)
public final FloatBuffer put(float[] src)
public FloatBuffer put(float[] src, int offset, int length)
public abstract FloatBuffer put(int index, float f)
public FloatBuffer put(FloatBuffer src)
~~~

## Parámetros
* **float f**,  {% include w3api/param_description.html metodo=_dato parametro="float f" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **float[] src**,  {% include w3api/param_description.html metodo=_dato parametro="float[] src" %}
* **FloatBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="FloatBuffer src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
