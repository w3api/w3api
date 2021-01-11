---
title: QuadCurve2D.subdivide()
permalink: Java/QuadCurve2D/subdivide
date: 2021-01-11
key: JavaJava.Q.QuadCurve2D
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Q.QuadCurve2D.metodos valor="subdivide" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void subdivide(double[] src, int srcoff, double[] left, int leftoff, double[] right, int rightoff)
public void subdivide(QuadCurve2D left, QuadCurve2D right)
public static void subdivide(QuadCurve2D src, QuadCurve2D left, QuadCurve2D right)
~~~

## Parámetros
* **QuadCurve2D left**,  {% include w3api/param_description.html metodo=_dato parametro="QuadCurve2D left" %}
* **QuadCurve2D src**,  {% include w3api/param_description.html metodo=_dato parametro="QuadCurve2D src" %}
* **int leftoff**,  {% include w3api/param_description.html metodo=_dato parametro="int leftoff" %}
* **double[] src**,  {% include w3api/param_description.html metodo=_dato parametro="double[] src" %}
* **QuadCurve2D right**,  {% include w3api/param_description.html metodo=_dato parametro="QuadCurve2D right" %}
* **double[] left**,  {% include w3api/param_description.html metodo=_dato parametro="double[] left" %}
* **int srcoff**,  {% include w3api/param_description.html metodo=_dato parametro="int srcoff" %}
* **int rightoff**,  {% include w3api/param_description.html metodo=_dato parametro="int rightoff" %}
* **double[] right**,  {% include w3api/param_description.html metodo=_dato parametro="double[] right" %}

## Clase Padre
[QuadCurve2D](/Java/QuadCurve2D/)

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
