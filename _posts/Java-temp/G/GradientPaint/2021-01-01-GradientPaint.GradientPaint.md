---
title: GradientPaint.GradientPaint()
permalink: /Java/GradientPaint/GradientPaint/
date: 2021-01-11
key: Java.G.GradientPaint
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GradientPaint.constructores valor="GradientPaint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GradientPaint(float x1, float y1, Color color1, float x2, float y2, Color color2)
public GradientPaint(float x1, float y1, Color color1, float x2, float y2, Color color2, boolean cyclic)
public GradientPaint(Point2D pt1, Color color1, Point2D pt2, Color color2)
@ConstructorProperties({"point1","color1","point2","color2","cyclic"}) public GradientPaint(Point2D pt1, Color color1, Point2D pt2, Color color2, boolean cyclic)
~~~

## Parámetros
* **float y2**,  {% include w3api/param_description.html metodo=_dato parametro="float y2" %}
* **boolean cyclic**,  {% include w3api/param_description.html metodo=_dato parametro="boolean cyclic" %}
* **float y1**,  {% include w3api/param_description.html metodo=_dato parametro="float y1" %}
* **float x1**,  {% include w3api/param_description.html metodo=_dato parametro="float x1" %}
* **Color color1**,  {% include w3api/param_description.html metodo=_dato parametro="Color color1" %}
* **float x2**,  {% include w3api/param_description.html metodo=_dato parametro="float x2" %}
* **Point2D pt1**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D pt1" %}
* **Point2D pt2**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D pt2" %}
* **Color color2**,  {% include w3api/param_description.html metodo=_dato parametro="Color color2" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[GradientPaint](/Java/GradientPaint/)

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
