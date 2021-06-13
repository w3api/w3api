---
title: CubicCurve2D.intersects()
permalink: /Java/CubicCurve2D/intersects/
date: 2021-01-11
key: Java.C.CubicCurve2D
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CubicCurve2D.metodos valor="intersects" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean intersects(double x, double y, double w, double h)
public boolean intersects(Rectangle2D r)
~~~

## Parámetros
* **double h**,  {% include w3api/param_description.html metodo=_dato parametro="double h" %}
* **double w**,  {% include w3api/param_description.html metodo=_dato parametro="double w" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **Rectangle2D r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D r" %}

## Clase Padre
[CubicCurve2D](/Java/CubicCurve2D/)

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
