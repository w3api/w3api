---
title: NumberAxis.NumberAxis()
permalink: Java/NumberAxis/NumberAxis
date: 2021-01-11
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
* **String axisLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String axisLabel" %}
* **double lowerBound**,  {% include w3api/param_description.html metodo=_dato parametro="double lowerBound" %}
* **double tickUnit**,  {% include w3api/param_description.html metodo=_dato parametro="double tickUnit" %}
* **double upperBound**,  {% include w3api/param_description.html metodo=_dato parametro="double upperBound" %}

## Clase Padre
[NumberAxis](/Java/NumberAxis/)

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
