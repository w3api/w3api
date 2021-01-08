---
title: FlatteningPathIterator.FlatteningPathIterator()
permalink: Java/FlatteningPathIterator/FlatteningPathIterator
date: 2021-01-04
key: JavaJava.F.FlatteningPathIterator
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlatteningPathIterator.constructores valor="FlatteningPathIterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FlatteningPathIterator(PathIterator src, double flatness)
public FlatteningPathIterator(PathIterator src, double flatness, int limit)
~~~

## Parámetros
* **PathIterator src**,  {% include w3api/param_description.html metodo=_data parametro="PathIterator src" %}
* **int limit**,  {% include w3api/param_description.html metodo=_data parametro="int limit" %}
* **double flatness**,  {% include w3api/param_description.html metodo=_data parametro="double flatness" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FlatteningPathIterator](/Java/FlatteningPathIterator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FlatteningPathIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
