---
title: RectangularShape.setFrame()
permalink: Java/RectangularShape/setFrame
date: 2021-01-11
key: JavaJava.R.RectangularShape
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RectangularShape.metodos valor="setFrame" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setFrame(double x, double y, double w, double h)
public void setFrame(Point2D loc, Dimension2D size)
public void setFrame(Rectangle2D r)
~~~

## Parámetros
* **double h**,  {% include w3api/param_description.html metodo=_dato parametro="double h" %}
* **double w**,  {% include w3api/param_description.html metodo=_dato parametro="double w" %}
* **Dimension2D size**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension2D size" %}
* **Point2D loc**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D loc" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **Rectangle2D r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D r" %}

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
