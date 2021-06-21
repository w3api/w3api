---
title: CubicCurve2D.solveCubic()
permalink: /Java/CubicCurve2D/solveCubic/
date: 2021-01-11
key: Java.C.CubicCurve2D
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CubicCurve2D.metodos valor="solveCubic" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int solveCubic(double[] eqn)
public static int solveCubic(double[] eqn, double[] res)
~~~

## Parámetros
* **double[] res**,  {% include w3api/param_description.html metodo=_dato parametro="double[] res" %}
* **double[] eqn**,  {% include w3api/param_description.html metodo=_dato parametro="double[] eqn" %}

## Clase Padre
[CubicCurve2D](/Java/CubicCurve2D/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
