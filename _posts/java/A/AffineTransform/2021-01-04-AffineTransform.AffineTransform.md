---
title: AffineTransform.AffineTransform()
permalink: Java/AffineTransform/AffineTransform
date: 2021-01-04
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
* **AffineTransform Tx**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform Tx" %}
* **float[] flatmatrix**,  {% include w3api/param_description.html metodo=_data parametro="float[] flatmatrix" %}
* **float m01**,  {% include w3api/param_description.html metodo=_data parametro="float m01" %}
* **double m12**,  {% include w3api/param_description.html metodo=_data parametro="double m12" %}
* **double m10**,  {% include w3api/param_description.html metodo=_data parametro="double m10" %}
* **float m02**,  {% include w3api/param_description.html metodo=_data parametro="float m02" %}
* **float m10**,  {% include w3api/param_description.html metodo=_data parametro="float m10" %}
* **double m01**,  {% include w3api/param_description.html metodo=_data parametro="double m01" %}
* **double m11**,  {% include w3api/param_description.html metodo=_data parametro="double m11" %}
* **float m12**,  {% include w3api/param_description.html metodo=_data parametro="float m12" %}
* **double[] flatmatrix**,  {% include w3api/param_description.html metodo=_data parametro="double[] flatmatrix" %}
* **float m00**,  {% include w3api/param_description.html metodo=_data parametro="float m00" %}
* **double m02**,  {% include w3api/param_description.html metodo=_data parametro="double m02" %}
* **double m00**,  {% include w3api/param_description.html metodo=_data parametro="double m00" %}
* **float m11**,  {% include w3api/param_description.html metodo=_data parametro="float m11" %}

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
