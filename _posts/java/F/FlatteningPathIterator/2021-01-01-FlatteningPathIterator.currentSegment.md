---
title: FlatteningPathIterator.currentSegment()
permalink: Java/FlatteningPathIterator/currentSegment
date: 2021-01-11
key: JavaJava.F.FlatteningPathIterator
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlatteningPathIterator.metodos valor="currentSegment" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int currentSegment(double[] coords)
public int currentSegment(float[] coords)
~~~

## Parámetros
* **float[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="float[] coords" %}
* **double[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="double[] coords" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/)

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
