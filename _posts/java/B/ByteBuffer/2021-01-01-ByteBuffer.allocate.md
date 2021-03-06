---
title: ByteBuffer.allocate()
permalink: /Java/ByteBuffer/allocate/
date: 2021-01-11
key: Java.B.ByteBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteBuffer.metodos valor="allocate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ByteBuffer allocate(int capacity)
~~~

## Parámetros
* **int capacity**,  {% include w3api/param_description.html metodo=_dato parametro="int capacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
