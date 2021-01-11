---
title: PathIterator.currentSegment()
permalink: Java/PathIterator/currentSegment
date: 2021-01-11
key: JavaJava.P.PathIterator
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PathIterator.metodos valor="currentSegment" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int currentSegment(double[] coords)
int currentSegment(float[] coords)
~~~

## Parámetros
* **float[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="float[] coords" %}
* **double[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="double[] coords" %}

## Clase Padre
[PathIterator](/Java/PathIterator/)

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
