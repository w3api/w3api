---
title: ShortBuffer.put()
permalink: Java/ShortBuffer/put
date: 2021-01-04
key: JavaJava.S.ShortBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ShortBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ShortBuffer put(int index, short s)
public abstract ShortBuffer put(short s)
public final ShortBuffer put(short[] src)
public ShortBuffer put(short[] src, int offset, int length)
public ShortBuffer put(ShortBuffer src)
~~~

## Parámetros
* **ShortBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="ShortBuffer src" %}
* **short s**,  {% include w3api/param_description.html metodo=_data parametro="short s" %}
* **short[] src**,  {% include w3api/param_description.html metodo=_data parametro="short[] src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ShortBuffer](/Java/ShortBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ShortBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
