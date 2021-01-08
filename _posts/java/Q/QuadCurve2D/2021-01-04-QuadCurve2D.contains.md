---
title: QuadCurve2D.contains()
permalink: Java/QuadCurve2D/contains
date: 2021-01-04
key: JavaJava.Q.QuadCurve2D
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Q.QuadCurve2D.metodos valor="contains" %}

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
* **Rectangle2D r**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle2D r" %}
* **double w**,  {% include w3api/param_description.html metodo=_data parametro="double w" %}
* **double h**,  {% include w3api/param_description.html metodo=_data parametro="double h" %}
* **Point2D p**,  {% include w3api/param_description.html metodo=_data parametro="Point2D p" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}

## Clase Padre
[QuadCurve2D](/Java/QuadCurve2D/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Q.QuadCurve2D.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
