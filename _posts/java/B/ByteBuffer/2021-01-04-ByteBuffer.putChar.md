---
title: ByteBuffer.putChar()
permalink: Java/ByteBuffer/putChar
date: 2021-01-04
key: JavaJava.B.ByteBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="putChar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ByteBuffer putChar(char value)
public abstract ByteBuffer putChar(int index, char value)
~~~

## Parámetros
* **char value**,  {% include w3api/param_description.html metodo=_data parametro="char value" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[ByteBuffer](/Java/ByteBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.ByteBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
