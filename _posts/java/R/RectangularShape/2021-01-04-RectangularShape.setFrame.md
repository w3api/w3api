---
title: RectangularShape.setFrame()
permalink: Java/RectangularShape/setFrame
date: 2021-01-04
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
* **Point2D loc**,  {% include w3api/param_description.html metodo=_data parametro="Point2D loc" %}
* **double w**,  {% include w3api/param_description.html metodo=_data parametro="double w" %}
* **Rectangle2D r**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle2D r" %}
* **double h**,  {% include w3api/param_description.html metodo=_data parametro="double h" %}
* **Dimension2D size**,  {% include w3api/param_description.html metodo=_data parametro="Dimension2D size" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}

## Clase Padre
[RectangularShape](/Java/RectangularShape/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RectangularShape.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
