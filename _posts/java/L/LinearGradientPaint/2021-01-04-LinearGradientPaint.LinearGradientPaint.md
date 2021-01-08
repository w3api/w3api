---
title: LinearGradientPaint.LinearGradientPaint()
permalink: Java/LinearGradientPaint/LinearGradientPaint
date: 2021-01-04
key: JavaJava.L.LinearGradientPaint
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
* **Point2D end**,  {% include w3api/param_description.html metodo=_data parametro="Point2D end" %}
* **float endX**,  {% include w3api/param_description.html metodo=_data parametro="float endX" %}
* **float endY**,  {% include w3api/param_description.html metodo=_data parametro="float endY" %}
* **float[] fractions**,  {% include w3api/param_description.html metodo=_data parametro="float[] fractions" %}
* **MultipleGradientPaint.CycleMethod cycleMethod**,  {% include w3api/param_description.html metodo=_data parametro="MultipleGradientPaint.CycleMethod cycleMethod" %}
* **AffineTransform gradientTransform**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform gradientTransform" %}
* **float startX**,  {% include w3api/param_description.html metodo=_data parametro="float startX" %}
* **float startY**,  {% include w3api/param_description.html metodo=_data parametro="float startY" %}
* **MultipleGradientPaint.ColorSpaceType colorSpace**,  {% include w3api/param_description.html metodo=_data parametro="MultipleGradientPaint.ColorSpaceType colorSpace" %}
* **Point2D start**,  {% include w3api/param_description.html metodo=_data parametro="Point2D start" %}
* **Color[] colors**,  {% include w3api/param_description.html metodo=_data parametro="Color[] colors" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LinearGradientPaint](/Java/LinearGradientPaint/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinearGradientPaint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
