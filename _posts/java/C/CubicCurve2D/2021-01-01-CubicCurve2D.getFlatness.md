---
title: CubicCurve2D.getFlatness()
permalink: /Java/CubicCurve2D/getFlatness/
date: 2021-01-11
key: Java.C.CubicCurve2D
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CubicCurve2D.metodos valor="getFlatness" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double getFlatness()
public static double getFlatness(double[] coords, int offset)
public static double getFlatness(double x1, double y1, double ctrlx1, double ctrly1, double ctrlx2, double ctrly2, double x2, double y2)
~~~

## Parámetros
* **double ctrly1**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrly1" %}
* **double x1**,  {% include w3api/param_description.html metodo=_dato parametro="double x1" %}
* **double y2**,  {% include w3api/param_description.html metodo=_dato parametro="double y2" %}
* **double y1**,  {% include w3api/param_description.html metodo=_dato parametro="double y1" %}
* **double ctrlx2**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrlx2" %}
* **double ctrlx1**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrlx1" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **double[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="double[] coords" %}
* **double x2**,  {% include w3api/param_description.html metodo=_dato parametro="double x2" %}
* **double ctrly2**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrly2" %}

## Clase Padre
[CubicCurve2D](/Java/CubicCurve2D/)

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
