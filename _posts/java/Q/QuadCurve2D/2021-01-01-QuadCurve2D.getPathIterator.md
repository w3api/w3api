---
title: QuadCurve2D.getPathIterator()
permalink: Java/QuadCurve2D/getPathIterator
date: 2021-01-11
key: JavaJava.Q.QuadCurve2D
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Q.QuadCurve2D.metodos valor="getPathIterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PathIterator getPathIterator(AffineTransform at)
public PathIterator getPathIterator(AffineTransform at, double flatness)
~~~

## Parámetros
* **AffineTransform at**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform at" %}
* **double flatness**,  {% include w3api/param_description.html metodo=_dato parametro="double flatness" %}

## Clase Padre
[QuadCurve2D](/Java/QuadCurve2D/)

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
