---
title: GradientPaint.GradientPaint()
permalink: Java/GradientPaint/GradientPaint
date: 2021-01-04
key: JavaJava.G.GradientPaint
category: java
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
* **float y1**,  {% include w3api/param_description.html metodo=_data parametro="float y1" %}
* **Point2D pt2**,  {% include w3api/param_description.html metodo=_data parametro="Point2D pt2" %}
* **float y2**,  {% include w3api/param_description.html metodo=_data parametro="float y2" %}
* **Point2D pt1**,  {% include w3api/param_description.html metodo=_data parametro="Point2D pt1" %}
* **Color color2**,  {% include w3api/param_description.html metodo=_data parametro="Color color2" %}
* **Color color1**,  {% include w3api/param_description.html metodo=_data parametro="Color color1" %}
* **float x1**,  {% include w3api/param_description.html metodo=_data parametro="float x1" %}
* **boolean cyclic**,  {% include w3api/param_description.html metodo=_data parametro="boolean cyclic" %}
* **float x2**,  {% include w3api/param_description.html metodo=_data parametro="float x2" %}

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
{%- for _ldc in site.data.Java.G.GradientPaint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
