---
title: QuadCurve2D.getFlatness()
permalink: /Java/QuadCurve2D/getFlatness/
date: 2021-01-11
key: Java.Q.QuadCurve2D
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Q.QuadCurve2D.metodos valor="getFlatness" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double getFlatness()
public static double getFlatness(double[] coords, int offset)
public static double getFlatness(double x1, double y1, double ctrlx, double ctrly, double x2, double y2)
~~~

## Parámetros
* **double ctrly**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrly" %}
* **double x1**,  {% include w3api/param_description.html metodo=_dato parametro="double x1" %}
* **double y2**,  {% include w3api/param_description.html metodo=_dato parametro="double y2" %}
* **double y1**,  {% include w3api/param_description.html metodo=_dato parametro="double y1" %}
* **double ctrlx**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrlx" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **double[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="double[] coords" %}
* **double x2**,  {% include w3api/param_description.html metodo=_dato parametro="double x2" %}

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
