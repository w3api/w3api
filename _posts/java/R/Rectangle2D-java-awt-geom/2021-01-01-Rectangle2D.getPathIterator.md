---
title: Rectangle2D.getPathIterator()
permalink: Java/Rectangle2D-java-awt-geom/getPathIterator
date: 2021-01-11
key: JavaJava.R.Rectangle2D-java-awt-geom
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Rectangle2D-java-awt-geom.metodos valor="getPathIterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PathIterator getPathIterator(AffineTransform at)
public PathIterator getPathIterator(AffineTransform at, double flatness)
~~~

## Parámetros
* **AffineTransform at**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform at" %}
* **double flatness**,  {% include w3api/param_description.html metodo=_dato parametro="double flatness" %}

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
