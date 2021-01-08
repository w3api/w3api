---
title: CubicCurve2D.subdivide()
permalink: Java/CubicCurve2D/subdivide
date: 2021-01-04
key: JavaJava.C.CubicCurve2D
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CubicCurve2D.metodos valor="subdivide" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void subdivide(double[] src, int srcoff, double[] left, int leftoff, double[] right, int rightoff)
public void subdivide(CubicCurve2D left, CubicCurve2D right)
public static void subdivide(CubicCurve2D src, CubicCurve2D left, CubicCurve2D right)
~~~

## Parámetros
* **int rightoff**,  {% include w3api/param_description.html metodo=_data parametro="int rightoff" %}
* **CubicCurve2D right**,  {% include w3api/param_description.html metodo=_data parametro="CubicCurve2D right" %}
* **CubicCurve2D src**,  {% include w3api/param_description.html metodo=_data parametro="CubicCurve2D src" %}
* **int srcoff**,  {% include w3api/param_description.html metodo=_data parametro="int srcoff" %}
* **double[] left**,  {% include w3api/param_description.html metodo=_data parametro="double[] left" %}
* **CubicCurve2D left**,  {% include w3api/param_description.html metodo=_data parametro="CubicCurve2D left" %}
* **double[] right**,  {% include w3api/param_description.html metodo=_data parametro="double[] right" %}
* **double[] src**,  {% include w3api/param_description.html metodo=_data parametro="double[] src" %}
* **int leftoff**,  {% include w3api/param_description.html metodo=_data parametro="int leftoff" %}

## Clase Padre
[CubicCurve2D](/Java/CubicCurve2D/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CubicCurve2D.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
