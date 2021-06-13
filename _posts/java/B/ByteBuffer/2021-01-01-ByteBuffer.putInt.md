---
title: ByteBuffer.putInt()
permalink: /Java/ByteBuffer/putInt/
date: 2021-01-11
key: JavaJava.B.ByteBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="putInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ByteBuffer putInt(int value)
public abstract ByteBuffer putInt(int index, int value)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/)

## Clase Padre
[ByteBuffer](/Java/ByteBuffer/)

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
