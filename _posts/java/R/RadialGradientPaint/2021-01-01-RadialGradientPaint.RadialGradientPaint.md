---
title: RadialGradientPaint.RadialGradientPaint()
permalink: Java/RadialGradientPaint/RadialGradientPaint
date: 2021-01-11
key: Java.R.RadialGradientPaint
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RadialGradientPaint.constructores valor="RadialGradientPaint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RadialGradientPaint(float cx, float cy, float radius, float[] fractions, Color[] colors)
public RadialGradientPaint(float cx, float cy, float radius, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
public RadialGradientPaint(float cx, float cy, float radius, float fx, float fy, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
public RadialGradientPaint(Point2D center, float radius, float[] fractions, Color[] colors)
public RadialGradientPaint(Point2D center, float radius, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
public RadialGradientPaint(Point2D center, float radius, Point2D focus, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
@ConstructorProperties({"centerPoint","radius","focusPoint","fractions","colors","cycleMethod","colorSpace","transform"}) public RadialGradientPaint(Point2D center, float radius, Point2D focus, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod, MultipleGradientPaint.ColorSpaceType colorSpace, AffineTransform gradientTransform)
public RadialGradientPaint(Rectangle2D gradientBounds, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
~~~

## Parámetros
* **float cy**,  {% include w3api/param_description.html metodo=_dato parametro="float cy" %}
* **float cx**,  {% include w3api/param_description.html metodo=_dato parametro="float cx" %}
* **float[] fractions**,  {% include w3api/param_description.html metodo=_dato parametro="float[] fractions" %}
* **float fy**,  {% include w3api/param_description.html metodo=_dato parametro="float fy" %}
* **MultipleGradientPaint.ColorSpaceType colorSpace**,  {% include w3api/param_description.html metodo=_dato parametro="MultipleGradientPaint.ColorSpaceType colorSpace" %}
* **float radius**,  {% include w3api/param_description.html metodo=_dato parametro="float radius" %}
* **Point2D focus**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D focus" %}
* **Color[] colors**,  {% include w3api/param_description.html metodo=_dato parametro="Color[] colors" %}
* **MultipleGradientPaint.CycleMethod cycleMethod**,  {% include w3api/param_description.html metodo=_dato parametro="MultipleGradientPaint.CycleMethod cycleMethod" %}
* **Point2D center**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D center" %}
* **AffineTransform gradientTransform**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform gradientTransform" %}
* **Rectangle2D gradientBounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D gradientBounds" %}
* **float fx**,  {% include w3api/param_description.html metodo=_dato parametro="float fx" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RadialGradientPaint](/Java/RadialGradientPaint/)

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
