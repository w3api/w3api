---
title: ByteBuffer.putFloat()
permalink: /Java/ByteBuffer/putFloat/
date: 2021-01-11
key: Java.B.ByteBuffer
category: Java
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
* **float value**,  {% include w3api/param_description.html metodo=_dato parametro="float value" %}
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
