---
title: AffineTransform.deltaTransform()
permalink: Java/AffineTransform/deltaTransform
date: 2021-01-04
key: JavaJava.A.AffineTransform
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransform.metodos valor="deltaTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void deltaTransform(double[] srcPts, int srcOff, double[] dstPts, int dstOff, int numPts)
public Point2D deltaTransform(Point2D ptSrc, Point2D ptDst)
~~~

## Parámetros
* **int dstOff**,  {% include w3api/param_description.html metodo=_data parametro="int dstOff" %}
* **double[] srcPts**,  {% include w3api/param_description.html metodo=_data parametro="double[] srcPts" %}
* **Point2D ptDst**,  {% include w3api/param_description.html metodo=_data parametro="Point2D ptDst" %}
* **int numPts**,  {% include w3api/param_description.html metodo=_data parametro="int numPts" %}
* **Point2D ptSrc**,  {% include w3api/param_description.html metodo=_data parametro="Point2D ptSrc" %}
* **int srcOff**,  {% include w3api/param_description.html metodo=_data parametro="int srcOff" %}
* **double[] dstPts**,  {% include w3api/param_description.html metodo=_data parametro="double[] dstPts" %}

## Clase Padre
[AffineTransform](/Java/AffineTransform/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AffineTransform.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
