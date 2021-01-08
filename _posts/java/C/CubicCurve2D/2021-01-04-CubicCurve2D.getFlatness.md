---
title: CubicCurve2D.getFlatness()
permalink: Java/CubicCurve2D/getFlatness
date: 2021-01-04
key: JavaJava.C.CubicCurve2D
category: java
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
* **double[] coords**,  {% include w3api/param_description.html metodo=_data parametro="double[] coords" %}
* **double y1**,  {% include w3api/param_description.html metodo=_data parametro="double y1" %}
* **double y2**,  {% include w3api/param_description.html metodo=_data parametro="double y2" %}
* **double ctrlx1**,  {% include w3api/param_description.html metodo=_data parametro="double ctrlx1" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **double ctrly1**,  {% include w3api/param_description.html metodo=_data parametro="double ctrly1" %}
* **double x2**,  {% include w3api/param_description.html metodo=_data parametro="double x2" %}
* **double ctrly2**,  {% include w3api/param_description.html metodo=_data parametro="double ctrly2" %}
* **double x1**,  {% include w3api/param_description.html metodo=_data parametro="double x1" %}
* **double ctrlx2**,  {% include w3api/param_description.html metodo=_data parametro="double ctrlx2" %}

## Clase Padre
[CubicCurve2D](/Java/CubicCurve2D/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CubicCurve2D.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
