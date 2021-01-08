---
title: NumberAxis.NumberAxis()
permalink: Java/NumberAxis/NumberAxis
date: 2021-01-04
key: JavaJava.N.NumberAxis
category: java
tags: ['java se', 'javafx.scene.chart', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberAxis.constructores valor="NumberAxis" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NumberAxis()
public NumberAxis(double lowerBound, double upperBound, double tickUnit)
public NumberAxis(String axisLabel, double lowerBound, double upperBound, double tickUnit)
~~~

## Parámetros
* **double tickUnit**,  {% include w3api/param_description.html metodo=_data parametro="double tickUnit" %}
* **double upperBound**,  {% include w3api/param_description.html metodo=_data parametro="double upperBound" %}
* **double lowerBound**,  {% include w3api/param_description.html metodo=_data parametro="double lowerBound" %}
* **String axisLabel**,  {% include w3api/param_description.html metodo=_data parametro="String axisLabel" %}

## Clase Padre
[NumberAxis](/Java/NumberAxis/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumberAxis.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
