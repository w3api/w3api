---
title: CubicCurve2D.setCurve()
permalink: Java/CubicCurve2D/setCurve
date: 2021-01-04
key: JavaJava.C.CubicCurve2D
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CubicCurve2D.metodos valor="setCurve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setCurve(double[] coords, int offset)
public abstract void setCurve(double x1, double y1, double ctrlx1, double ctrly1, double ctrlx2, double ctrly2, double x2, double y2)
public void setCurve(CubicCurve2D c)
public void setCurve(Point2D[] pts, int offset)
public void setCurve(Point2D p1, Point2D cp1, Point2D cp2, Point2D p2)
~~~

## Parámetros
* **double[] coords**,  {% include w3api/param_description.html metodo=_data parametro="double[] coords" %}
* **double y1**,  {% include w3api/param_description.html metodo=_data parametro="double y1" %}
* **Point2D cp2**,  {% include w3api/param_description.html metodo=_data parametro="Point2D cp2" %}
* **Point2D[] pts**,  {% include w3api/param_description.html metodo=_data parametro="Point2D[] pts" %}
* **double y2**,  {% include w3api/param_description.html metodo=_data parametro="double y2" %}
* **double ctrlx1**,  {% include w3api/param_description.html metodo=_data parametro="double ctrlx1" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **double ctrly1**,  {% include w3api/param_description.html metodo=_data parametro="double ctrly1" %}
* **double x2**,  {% include w3api/param_description.html metodo=_data parametro="double x2" %}
* **double ctrly2**,  {% include w3api/param_description.html metodo=_data parametro="double ctrly2" %}
* **CubicCurve2D c**,  {% include w3api/param_description.html metodo=_data parametro="CubicCurve2D c" %}
* **Point2D p2**,  {% include w3api/param_description.html metodo=_data parametro="Point2D p2" %}
* **Point2D p1**,  {% include w3api/param_description.html metodo=_data parametro="Point2D p1" %}
* **double x1**,  {% include w3api/param_description.html metodo=_data parametro="double x1" %}
* **Point2D cp1**,  {% include w3api/param_description.html metodo=_data parametro="Point2D cp1" %}
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
