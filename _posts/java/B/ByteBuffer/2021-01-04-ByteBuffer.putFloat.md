---
title: ByteBuffer.putFloat()
permalink: Java/ByteBuffer/putFloat
date: 2021-01-04
key: JavaJava.B.ByteBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="putFloat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ByteBuffer putFloat(float value)
public abstract ByteBuffer putFloat(int index, float value)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **float value**,  {% include w3api/param_description.html metodo=_data parametro="float value" %}

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
