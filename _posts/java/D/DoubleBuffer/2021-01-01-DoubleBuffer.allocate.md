---
title: DoubleBuffer.allocate()
permalink: Java/DoubleBuffer/allocate
date: 2021-01-11
key: JavaJava.D.DoubleBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleBuffer.metodos valor="allocate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DoubleBuffer allocate(int capacity)
~~~

## Parámetros
* **int capacity**,  {% include w3api/param_description.html metodo=_dato parametro="int capacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DoubleBuffer](/Java/DoubleBuffer/)

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
