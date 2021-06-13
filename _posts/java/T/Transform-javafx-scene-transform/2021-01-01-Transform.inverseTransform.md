---
title: Transform.inverseTransform()
permalink: /Java/Transform-javafx-scene-transform/inverseTransform/
date: 2021-01-11
key: Java.T.Transform-javafx-scene-transform
category: Java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="inverseTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Point2D inverseTransform(double x, double y) throws NonInvertibleTransformException
public Point3D inverseTransform(double x, double y, double z) throws NonInvertibleTransformException
public Bounds inverseTransform(Bounds bounds) throws NonInvertibleTransformException
public Point2D inverseTransform(Point2D point) throws NonInvertibleTransformException
public Point3D inverseTransform(Point3D point) throws NonInvertibleTransformException
~~~

## Parámetros
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **Point3D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point3D point" %}
* **Bounds bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Bounds bounds" %}
* **double z**,  {% include w3api/param_description.html metodo=_dato parametro="double z" %}
* **Point2D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D point" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalStateException](/Java/IllegalStateException/), [NonInvertibleTransformException](/Java/NonInvertibleTransformException/)

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
