---
title: QuadCurve2D.getFlatnessSq()
permalink: Java/QuadCurve2D/getFlatnessSq
date: 2021-01-04
key: JavaJava.Q.QuadCurve2D
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Q.QuadCurve2D.metodos valor="getFlatnessSq" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double getFlatnessSq()
public static double getFlatnessSq(double[] coords, int offset)
public static double getFlatnessSq(double x1, double y1, double ctrlx, double ctrly, double x2, double y2)
~~~

## Parámetros
* **double[] coords**,  {% include w3api/param_description.html metodo=_data parametro="double[] coords" %}
* **double ctrly**,  {% include w3api/param_description.html metodo=_data parametro="double ctrly" %}
* **double y1**,  {% include w3api/param_description.html metodo=_data parametro="double y1" %}
* **double y2**,  {% include w3api/param_description.html metodo=_data parametro="double y2" %}
* **double x2**,  {% include w3api/param_description.html metodo=_data parametro="double x2" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **double ctrlx**,  {% include w3api/param_description.html metodo=_data parametro="double ctrlx" %}
* **double x1**,  {% include w3api/param_description.html metodo=_data parametro="double x1" %}

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
