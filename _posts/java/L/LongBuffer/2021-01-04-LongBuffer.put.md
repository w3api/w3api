---
title: LongBuffer.put()
permalink: Java/LongBuffer/put
date: 2021-01-04
key: JavaJava.L.LongBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongBuffer.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract LongBuffer put(int index, long l)
public abstract LongBuffer put(long l)
public final LongBuffer put(long[] src)
public LongBuffer put(long[] src, int offset, int length)
public LongBuffer put(LongBuffer src)
~~~

## Parámetros
* **LongBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="LongBuffer src" %}
* **long[] src**,  {% include w3api/param_description.html metodo=_data parametro="long[] src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **long l**,  {% include w3api/param_description.html metodo=_data parametro="long l" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LongBuffer](/Java/LongBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
