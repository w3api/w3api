---
title: Transform.transform()
permalink: Java/Transform-javafx-scene-transform/transform
date: 2021-01-04
key: JavaJava.T.Transform-javafx-scene-transform
category: java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="transform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Point2D transform(double x, double y)
public Point3D transform(double x, double y, double z)
public Bounds transform(Bounds bounds)
public Point2D transform(Point2D point)
public Point3D transform(Point3D point)
~~~

## Parámetros
* **Point3D point**,  {% include w3api/param_description.html metodo=_data parametro="Point3D point" %}
* **Bounds bounds**,  {% include w3api/param_description.html metodo=_data parametro="Bounds bounds" %}
* **Point2D point**,  {% include w3api/param_description.html metodo=_data parametro="Point2D point" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **double z**,  {% include w3api/param_description.html metodo=_data parametro="double z" %}

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
{%- for _ldc in site.data.Java.T.Transform-javafx-scene-transform.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
