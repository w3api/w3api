---
title: Interpolator.interpolate()
permalink: Java/Interpolator/interpolate
date: 2021-01-04
key: JavaJava.I.Interpolator
category: java
tags: ['java se', 'javafx.animation', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Interpolator.metodos valor="interpolate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean interpolate(boolean startValue, boolean endValue, double fraction)
public double interpolate(double startValue, double endValue, double fraction)
public int interpolate(int startValue, int endValue, double fraction)
public long interpolate(long startValue, long endValue, double fraction)
public Object interpolate(Object startValue, Object endValue, double fraction)
~~~

## Parámetros
* **int endValue**,  {% include w3api/param_description.html metodo=_data parametro="int endValue" %}
* **double startValue**,  {% include w3api/param_description.html metodo=_data parametro="double startValue" %}
* **boolean endValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean endValue" %}
* **int startValue**,  {% include w3api/param_description.html metodo=_data parametro="int startValue" %}
* **Object startValue**,  {% include w3api/param_description.html metodo=_data parametro="Object startValue" %}
* **double fraction**,  {% include w3api/param_description.html metodo=_data parametro="double fraction" %}
* **boolean startValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean startValue" %}
* **long startValue**,  {% include w3api/param_description.html metodo=_data parametro="long startValue" %}
* **Object endValue**,  {% include w3api/param_description.html metodo=_data parametro="Object endValue" %}
* **long endValue**,  {% include w3api/param_description.html metodo=_data parametro="long endValue" %}
* **double endValue**,  {% include w3api/param_description.html metodo=_data parametro="double endValue" %}

## Clase Padre
[Interpolator](/Java/Interpolator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Interpolator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
