---
title: StackedBarChart.StackedBarChart()
permalink: Java/StackedBarChart/StackedBarChart
date: 2021-01-11
key: JavaJava.S.StackedBarChart
category: java
tags: ['java se', 'javafx.scene.chart', 'javafx.controls', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackedBarChart.constructores valor="StackedBarChart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StackedBarChart(Axis<X> xAxis, Axis<Y> yAxis)
public StackedBarChart(Axis<X> xAxis, Axis<Y> yAxis, ObservableList<XYChart.Series<X,Y>> data)
public StackedBarChart(Axis<X> xAxis, Axis<Y> yAxis, ObservableList<XYChart.Series<X,Y>> data, double categoryGap)
~~~

## Parámetros
* **double categoryGap**,  {% include w3api/param_description.html metodo=_dato parametro="double categoryGap" %}
* **ObservableList&lt;XYChart.Series&lt;X**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<XYChart.Series<X" %}
* **Y&gt;&gt; data**,  {% include w3api/param_description.html metodo=_dato parametro="Y>> data" %}
* **Axis&lt;Y&gt; yAxis**,  {% include w3api/param_description.html metodo=_dato parametro="Axis<Y> yAxis" %}
* **Axis&lt;X&gt; xAxis**,  {% include w3api/param_description.html metodo=_dato parametro="Axis<X> xAxis" %}

## Clase Padre
[StackedBarChart](/Java/StackedBarChart/)

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
