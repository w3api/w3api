---
title: AffineTransform.AffineTransform()
permalink: Java/AffineTransform/AffineTransform
date: 2021-01-11
key: JavaJava.A.AffineTransform
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransform.constructores valor="AffineTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AffineTransform()
public AffineTransform(double[] flatmatrix)
public AffineTransform(double m00, double m10, double m01, double m11, double m02, double m12)
public AffineTransform(float[] flatmatrix)
@ConstructorProperties({"scaleX","shearY","shearX","scaleY","translateX","translateY"}) public AffineTransform(float m00, float m10, float m01, float m11, float m02, float m12)
public AffineTransform(AffineTransform Tx)
~~~

## Parámetros
* **double m00**,  {% include w3api/param_description.html metodo=_dato parametro="double m00" %}
* **float m01**,  {% include w3api/param_description.html metodo=_dato parametro="float m01" %}
* **float m11**,  {% include w3api/param_description.html metodo=_dato parametro="float m11" %}
* **AffineTransform Tx**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform Tx" %}
* **double m10**,  {% include w3api/param_description.html metodo=_dato parametro="double m10" %}
* **float m10**,  {% include w3api/param_description.html metodo=_dato parametro="float m10" %}
* **float m00**,  {% include w3api/param_description.html metodo=_dato parametro="float m00" %}
* **double m12**,  {% include w3api/param_description.html metodo=_dato parametro="double m12" %}
* **double m01**,  {% include w3api/param_description.html metodo=_dato parametro="double m01" %}
* **float[] flatmatrix**,  {% include w3api/param_description.html metodo=_dato parametro="float[] flatmatrix" %}
* **float m02**,  {% include w3api/param_description.html metodo=_dato parametro="float m02" %}
* **float m12**,  {% include w3api/param_description.html metodo=_dato parametro="float m12" %}
* **double[] flatmatrix**,  {% include w3api/param_description.html metodo=_dato parametro="double[] flatmatrix" %}
* **double m11**,  {% include w3api/param_description.html metodo=_dato parametro="double m11" %}
* **double m02**,  {% include w3api/param_description.html metodo=_dato parametro="double m02" %}

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
