---
title: AffineTransform.inverseTransform()
permalink: /Java/AffineTransform/inverseTransform/
date: 2021-01-11
key: Java.A.AffineTransform
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransform.metodos valor="inverseTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void inverseTransform(double[] srcPts, int srcOff, double[] dstPts, int dstOff, int numPts) throws NoninvertibleTransformException
public Point2D inverseTransform(Point2D ptSrc, Point2D ptDst) throws NoninvertibleTransformException
~~~

## Parámetros
* **Point2D ptSrc**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D ptSrc" %}
* **int srcOff**,  {% include w3api/param_description.html metodo=_dato parametro="int srcOff" %}
* **double[] srcPts**,  {% include w3api/param_description.html metodo=_dato parametro="double[] srcPts" %}
* **int dstOff**,  {% include w3api/param_description.html metodo=_dato parametro="int dstOff" %}
* **double[] dstPts**,  {% include w3api/param_description.html metodo=_dato parametro="double[] dstPts" %}
* **Point2D ptDst**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D ptDst" %}
* **int numPts**,  {% include w3api/param_description.html metodo=_dato parametro="int numPts" %}

## Excepciones
[NoninvertibleTransformException](/Java/NoninvertibleTransformException/)

## Clase Padre
[AffineTransform](/Java/AffineTransform/)

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
