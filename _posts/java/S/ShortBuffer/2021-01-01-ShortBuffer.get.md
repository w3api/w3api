---
title: ShortBuffer.get()
permalink: Java/ShortBuffer/get
date: 2021-01-11
key: JavaJava.S.ShortBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ShortBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract short get()
public abstract short get(int index)
public ShortBuffer get(short[] dst)
public ShortBuffer get(short[] dst, int offset, int length)
~~~

## Parámetros
* **short[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="short[] dst" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BufferUnderflowException](/Java/BufferUnderflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[ShortBuffer](/Java/ShortBuffer/)

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
