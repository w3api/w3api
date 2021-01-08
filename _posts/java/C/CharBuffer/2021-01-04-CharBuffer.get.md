---
title: CharBuffer.get()
permalink: Java/CharBuffer/get
date: 2021-01-04
key: JavaJava.C.CharBuffer
category: java
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
* **char[] dst**,  {% include w3api/param_description.html metodo=_data parametro="char[] dst" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [BufferUnderflowException](/Java/BufferUnderflowException/)

## Clase Padre
[CharBuffer](/Java/CharBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
