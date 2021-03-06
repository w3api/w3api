---
title: FlatteningPathIterator.FlatteningPathIterator()
permalink: /Java/FlatteningPathIterator/FlatteningPathIterator/
date: 2021-01-11
key: Java.F.FlatteningPathIterator
category: Java
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
* **double flatness**,  {% include w3api/param_description.html metodo=_dato parametro="double flatness" %}
* **int limit**,  {% include w3api/param_description.html metodo=_dato parametro="int limit" %}
* **PathIterator src**,  {% include w3api/param_description.html metodo=_dato parametro="PathIterator src" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
