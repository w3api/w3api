---
title: BoundingBox.contains()
permalink: Java/BoundingBox/contains
date: 2021-01-11
key: JavaJava.B.BoundingBox
category: java
tags: ['java se', 'javafx.geometry', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BoundingBox.metodos valor="contains" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean contains(double x, double y)
public boolean contains(double x, double y, double z)
public boolean contains(double x, double y, double w, double h)
public boolean contains(double x, double y, double z, double w, double h, double d)
public boolean contains(Bounds b)
public boolean contains(Point2D p)
public boolean contains(Point3D p)
~~~

## Parámetros
* **Bounds b**,  {% include w3api/param_description.html metodo=_dato parametro="Bounds b" %}
* **double h**,  {% include w3api/param_description.html metodo=_dato parametro="double h" %}
* **double w**,  {% include w3api/param_description.html metodo=_dato parametro="double w" %}
* **double d**,  {% include w3api/param_description.html metodo=_dato parametro="double d" %}
* **Point3D p**,  {% include w3api/param_description.html metodo=_dato parametro="Point3D p" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **double z**,  {% include w3api/param_description.html metodo=_dato parametro="double z" %}
* **Point2D p**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D p" %}

## Clase Padre
[BoundingBox](/Java/BoundingBox/)

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
