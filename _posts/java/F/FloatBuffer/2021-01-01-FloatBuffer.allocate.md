---
title: FloatBuffer.allocate()
permalink: /Java/FloatBuffer/allocate/
date: 2021-01-11
key: Java.F.FloatBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FloatBuffer.metodos valor="allocate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static FloatBuffer allocate(int capacity)
~~~

## Parámetros
* **int capacity**,  {% include w3api/param_description.html metodo=_dato parametro="int capacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FloatBuffer](/Java/FloatBuffer/)

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
