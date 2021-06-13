---
title: LinearGradientPaint.LinearGradientPaint()
permalink: /Java/LinearGradientPaint/LinearGradientPaint/
date: 2021-01-11
key: Java.L.LinearGradientPaint
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinearGradientPaint.constructores valor="LinearGradientPaint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinearGradientPaint(float startX, float startY, float endX, float endY, float[] fractions, Color[] colors)
public LinearGradientPaint(float startX, float startY, float endX, float endY, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
public LinearGradientPaint(Point2D start, Point2D end, float[] fractions, Color[] colors)
public LinearGradientPaint(Point2D start, Point2D end, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod)
@ConstructorProperties({"startPoint","endPoint","fractions","colors","cycleMethod","colorSpace","transform"}) public LinearGradientPaint(Point2D start, Point2D end, float[] fractions, Color[] colors, MultipleGradientPaint.CycleMethod cycleMethod, MultipleGradientPaint.ColorSpaceType colorSpace, AffineTransform gradientTransform)
~~~

## Parámetros
* **float[] fractions**,  {% include w3api/param_description.html metodo=_dato parametro="float[] fractions" %}
* **MultipleGradientPaint.ColorSpaceType colorSpace**,  {% include w3api/param_description.html metodo=_dato parametro="MultipleGradientPaint.ColorSpaceType colorSpace" %}
* **Point2D end**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D end" %}
* **Color[] colors**,  {% include w3api/param_description.html metodo=_dato parametro="Color[] colors" %}
* **float endX**,  {% include w3api/param_description.html metodo=_dato parametro="float endX" %}
* **MultipleGradientPaint.CycleMethod cycleMethod**,  {% include w3api/param_description.html metodo=_dato parametro="MultipleGradientPaint.CycleMethod cycleMethod" %}
* **float startY**,  {% include w3api/param_description.html metodo=_dato parametro="float startY" %}
* **Point2D start**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D start" %}
* **AffineTransform gradientTransform**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform gradientTransform" %}
* **float endY**,  {% include w3api/param_description.html metodo=_dato parametro="float endY" %}
* **float startX**,  {% include w3api/param_description.html metodo=_dato parametro="float startX" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinearGradientPaint](/Java/LinearGradientPaint/)

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
