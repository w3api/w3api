---
title: BoundingBox.contains()
permalink: Java/BoundingBox/contains
date: 2021-01-04
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
* **double w**,  {% include w3api/param_description.html metodo=_data parametro="double w" %}
* **double h**,  {% include w3api/param_description.html metodo=_data parametro="double h" %}
* **double d**,  {% include w3api/param_description.html metodo=_data parametro="double d" %}
* **Point2D p**,  {% include w3api/param_description.html metodo=_data parametro="Point2D p" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **Point3D p**,  {% include w3api/param_description.html metodo=_data parametro="Point3D p" %}
* **double z**,  {% include w3api/param_description.html metodo=_data parametro="double z" %}
* **Bounds b**,  {% include w3api/param_description.html metodo=_data parametro="Bounds b" %}

## Clase Padre
[BoundingBox](/Java/BoundingBox/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BoundingBox.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
