---
title: Interpolator.interpolate()
permalink: /Java/Interpolator/interpolate/
date: 2021-01-11
key: Java.I.Interpolator
category: Java
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
* **int endValue**,  {% include w3api/param_description.html metodo=_dato parametro="int endValue" %}
* **long endValue**,  {% include w3api/param_description.html metodo=_dato parametro="long endValue" %}
* **double fraction**,  {% include w3api/param_description.html metodo=_dato parametro="double fraction" %}
* **boolean startValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean startValue" %}
* **double startValue**,  {% include w3api/param_description.html metodo=_dato parametro="double startValue" %}
* **int startValue**,  {% include w3api/param_description.html metodo=_dato parametro="int startValue" %}
* **double endValue**,  {% include w3api/param_description.html metodo=_dato parametro="double endValue" %}
* **Object startValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object startValue" %}
* **boolean endValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean endValue" %}
* **Object endValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object endValue" %}
* **long startValue**,  {% include w3api/param_description.html metodo=_dato parametro="long startValue" %}

## Clase Padre
[Interpolator](/Java/Interpolator/)

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
