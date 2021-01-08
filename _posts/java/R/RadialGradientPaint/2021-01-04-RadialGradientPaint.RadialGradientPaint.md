---
title: RadialGradientPaint.RadialGradientPaint()
permalink: Java/RadialGradientPaint/RadialGradientPaint
date: 2021-01-04
key: JavaJava.R.RadialGradientPaint
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
* **float cx**,  {% include w3api/param_description.html metodo=_data parametro="float cx" %}
* **float cy**,  {% include w3api/param_description.html metodo=_data parametro="float cy" %}
* **MultipleGradientPaint.CycleMethod cycleMethod**,  {% include w3api/param_description.html metodo=_data parametro="MultipleGradientPaint.CycleMethod cycleMethod" %}
* **float[] fractions**,  {% include w3api/param_description.html metodo=_data parametro="float[] fractions" %}
* **AffineTransform gradientTransform**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform gradientTransform" %}
* **float radius**,  {% include w3api/param_description.html metodo=_data parametro="float radius" %}
* **Point2D focus**,  {% include w3api/param_description.html metodo=_data parametro="Point2D focus" %}
* **Point2D center**,  {% include w3api/param_description.html metodo=_data parametro="Point2D center" %}
* **Rectangle2D gradientBounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle2D gradientBounds" %}
* **MultipleGradientPaint.ColorSpaceType colorSpace**,  {% include w3api/param_description.html metodo=_data parametro="MultipleGradientPaint.ColorSpaceType colorSpace" %}
* **float fy**,  {% include w3api/param_description.html metodo=_data parametro="float fy" %}
* **float fx**,  {% include w3api/param_description.html metodo=_data parametro="float fx" %}
* **Color[] colors**,  {% include w3api/param_description.html metodo=_data parametro="Color[] colors" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RadialGradientPaint](/Java/RadialGradientPaint/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RadialGradientPaint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
