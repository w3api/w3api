---
title: RadialGradient.RadialGradient()
permalink: Java/RadialGradient/RadialGradient
date: 2021-01-04
key: JavaJava.R.RadialGradient
category: java
tags: ['java se', 'javafx.scene.paint', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RadialGradient.constructores valor="RadialGradient" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RadialGradient(double focusAngle, double focusDistance, double centerX, double centerY, double radius, boolean proportional, CycleMethod cycleMethod, List<Stop> stops)
public RadialGradient(double focusAngle, double focusDistance, double centerX, double centerY, double radius, boolean proportional, CycleMethod cycleMethod, Stop... stops)
~~~

## Parámetros
* **double centerX**,  {% include w3api/param_description.html metodo=_data parametro="double centerX" %}
* **double radius**,  {% include w3api/param_description.html metodo=_data parametro="double radius" %}
* **double focusDistance**,  {% include w3api/param_description.html metodo=_data parametro="double focusDistance" %}
* **CycleMethod cycleMethod**,  {% include w3api/param_description.html metodo=_data parametro="CycleMethod cycleMethod" %}
* **Stop... stops**,  {% include w3api/param_description.html metodo=_data parametro="Stop... stops" %}
* **List&lt;Stop&gt; stops**,  {% include w3api/param_description.html metodo=_data parametro="List<Stop> stops" %}
* **double centerY**,  {% include w3api/param_description.html metodo=_data parametro="double centerY" %}
* **double focusAngle**,  {% include w3api/param_description.html metodo=_data parametro="double focusAngle" %}
* **boolean proportional**,  {% include w3api/param_description.html metodo=_data parametro="boolean proportional" %}

## Clase Padre
[RadialGradient](/Java/RadialGradient/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RadialGradient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
