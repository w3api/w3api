---
title: Rectangle2D.contains()
permalink: Java/Rectangle2D-javafx-geometry/contains
date: 2021-01-11
key: Java.R.Rectangle2D-javafx-geometry
category: java
tags: ['java se', 'javafx.geometry', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Rectangle2D-javafx-geometry.metodos valor="contains" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean contains(double x, double y)
public boolean contains(double x, double y, double w, double h)
public boolean contains(Point2D p)
public boolean contains(Rectangle2D r)
~~~

## Parámetros
* **double h**,  {% include w3api/param_description.html metodo=_dato parametro="double h" %}
* **double w**,  {% include w3api/param_description.html metodo=_dato parametro="double w" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **Rectangle2D r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D r" %}
* **Point2D p**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D p" %}

## Clase Padre
[Rectangle2D](/Java/Rectangle2D-javafx-geometry/)

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
