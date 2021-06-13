---
title: QuadCurve2D.setCurve()
permalink: /Java/QuadCurve2D/setCurve/
date: 2021-01-11
key: Java.Q.QuadCurve2D
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Q.QuadCurve2D.metodos valor="setCurve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setCurve(double[] coords, int offset)
public abstract void setCurve(double x1, double y1, double ctrlx, double ctrly, double x2, double y2)
public void setCurve(Point2D[] pts, int offset)
public void setCurve(Point2D p1, Point2D cp, Point2D p2)
public void setCurve(QuadCurve2D c)
~~~

## Parámetros
* **double ctrly**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrly" %}
* **double x1**,  {% include w3api/param_description.html metodo=_dato parametro="double x1" %}
* **double y2**,  {% include w3api/param_description.html metodo=_dato parametro="double y2" %}
* **Point2D p2**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D p2" %}
* **double y1**,  {% include w3api/param_description.html metodo=_dato parametro="double y1" %}
* **double ctrlx**,  {% include w3api/param_description.html metodo=_dato parametro="double ctrlx" %}
* **QuadCurve2D c**,  {% include w3api/param_description.html metodo=_dato parametro="QuadCurve2D c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **double[] coords**,  {% include w3api/param_description.html metodo=_dato parametro="double[] coords" %}
* **Point2D[] pts**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D[] pts" %}
* **double x2**,  {% include w3api/param_description.html metodo=_dato parametro="double x2" %}
* **Point2D cp**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D cp" %}
* **Point2D p1**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D p1" %}

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
