---
title: Transform.deltaTransform()
permalink: /Java/Transform-javafx-scene-transform/deltaTransform/
date: 2021-01-11
key: Java.T.Transform-javafx-scene-transform
category: Java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="deltaTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Point2D deltaTransform(double x, double y)
public Point3D deltaTransform(double x, double y, double z)
public Point2D deltaTransform(Point2D point)
public Point3D deltaTransform(Point3D point)
~~~

## Parámetros
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **Point3D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point3D point" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **double z**,  {% include w3api/param_description.html metodo=_dato parametro="double z" %}
* **Point2D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D point" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Transform](/Java/Transform-javafx-scene-transform/)

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
