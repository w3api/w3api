---
title: QuadCurve2D.subdivide()
permalink: Java/QuadCurve2D/subdivide
date: 2021-01-04
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
* **int rightoff**,  {% include w3api/param_description.html metodo=_data parametro="int rightoff" %}
* **QuadCurve2D src**,  {% include w3api/param_description.html metodo=_data parametro="QuadCurve2D src" %}
* **QuadCurve2D right**,  {% include w3api/param_description.html metodo=_data parametro="QuadCurve2D right" %}
* **int srcoff**,  {% include w3api/param_description.html metodo=_data parametro="int srcoff" %}
* **double[] left**,  {% include w3api/param_description.html metodo=_data parametro="double[] left" %}
* **double[] right**,  {% include w3api/param_description.html metodo=_data parametro="double[] right" %}
* **double[] src**,  {% include w3api/param_description.html metodo=_data parametro="double[] src" %}
* **int leftoff**,  {% include w3api/param_description.html metodo=_data parametro="int leftoff" %}
* **QuadCurve2D left**,  {% include w3api/param_description.html metodo=_data parametro="QuadCurve2D left" %}

## Clase Padre
[QuadCurve2D](/Java/QuadCurve2D/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Q.QuadCurve2D.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
