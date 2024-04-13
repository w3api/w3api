---
title: Rectangle2D.add()
permalink: /Java/Rectangle2D-java-awt-geom/add/
date: 2021-01-11
key: Java.R.Rectangle2D-java-awt-geom
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Rectangle2D-java-awt-geom.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(double newx, double newy)
public void add(Point2D pt)
public void add(Rectangle2D r)
~~~

## Parámetros
* **double newy**,  {% include w3api/param_description.html metodo=_dato parametro="double newy" %}
* **Point2D pt**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D pt" %}
* **Rectangle2D r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D r" %}
* **double newx**,  {% include w3api/param_description.html metodo=_dato parametro="double newx" %}

## Clase Padre
[Rectangle2D](/Java/Rectangle2D-java-awt-geom/)

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
