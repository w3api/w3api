---
title: ByteBuffer.alignedSlice()
permalink: /Java/ByteBuffer/alignedSlice/
date: 2021-01-11
key: Java.B.ByteBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="alignedSlice" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final ByteBuffer alignedSlice(int unitSize)
~~~

## Parámetros
* **int unitSize**,  {% include w3api/param_description.html metodo=_dato parametro="int unitSize" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
