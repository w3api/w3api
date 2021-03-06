---
title: RectangularShape.setFrameFromCenter()
permalink: /Java/RectangularShape/setFrameFromCenter/
date: 2021-01-11
key: Java.R.RectangularShape
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RectangularShape.metodos valor="setFrameFromCenter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFrameFromCenter(double centerX, double centerY, double cornerX, double cornerY)
public void setFrameFromCenter(Point2D center, Point2D corner)
~~~

## Parámetros
* **double centerY**,  {% include w3api/param_description.html metodo=_dato parametro="double centerY" %}
* **double cornerY**,  {% include w3api/param_description.html metodo=_dato parametro="double cornerY" %}
* **double centerX**,  {% include w3api/param_description.html metodo=_dato parametro="double centerX" %}
* **double cornerX**,  {% include w3api/param_description.html metodo=_dato parametro="double cornerX" %}
* **Point2D corner**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D corner" %}
* **Point2D center**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D center" %}

## Clase Padre
[RectangularShape](/Java/RectangularShape/)

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
