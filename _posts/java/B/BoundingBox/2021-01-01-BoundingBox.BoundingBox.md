---
title: BoundingBox.BoundingBox()
permalink: /Java/BoundingBox/BoundingBox/
date: 2021-01-11
key: Java.B.BoundingBox
category: java
tags: ['java se', 'javafx.geometry', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BoundingBox.constructores valor="BoundingBox" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BoundingBox(double minX, double minY, double width, double height)
public BoundingBox(double minX, double minY, double minZ, double width, double height, double depth)
~~~

## Parámetros
* **double minZ**,  {% include w3api/param_description.html metodo=_dato parametro="double minZ" %}
* **double minX**,  {% include w3api/param_description.html metodo=_dato parametro="double minX" %}
* **double minY**,  {% include w3api/param_description.html metodo=_dato parametro="double minY" %}
* **double width**,  {% include w3api/param_description.html metodo=_dato parametro="double width" %}
* **double height**,  {% include w3api/param_description.html metodo=_dato parametro="double height" %}
* **double depth**,  {% include w3api/param_description.html metodo=_dato parametro="double depth" %}

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
