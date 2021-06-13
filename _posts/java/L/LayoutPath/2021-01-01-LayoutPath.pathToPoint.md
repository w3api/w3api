---
title: LayoutPath.pathToPoint()
permalink: Java/LayoutPath/pathToPoint
date: 2021-01-11
key: Java.L.LayoutPath
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LayoutPath.metodos valor="pathToPoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void pathToPoint(Point2D location, boolean preceding, Point2D point)
~~~

## Parámetros
* **boolean preceding**,  {% include w3api/param_description.html metodo=_dato parametro="boolean preceding" %}
* **Point2D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D point" %}
* **Point2D location**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D location" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LayoutPath](/Java/LayoutPath/)

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
