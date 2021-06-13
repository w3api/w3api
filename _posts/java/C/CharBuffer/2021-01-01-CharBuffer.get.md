---
title: CharBuffer.get()
permalink: /Java/CharBuffer/get/
date: 2021-01-11
key: Java.C.CharBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharBuffer.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract char get()
public CharBuffer get(char[] dst)
public CharBuffer get(char[] dst, int offset, int length)
public abstract char get(int index)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **char[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="char[] dst" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BufferUnderflowException](/Java/BufferUnderflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CharBuffer](/Java/CharBuffer/)

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
