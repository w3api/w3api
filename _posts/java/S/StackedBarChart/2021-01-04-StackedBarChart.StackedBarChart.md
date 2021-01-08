---
title: StackedBarChart.StackedBarChart()
permalink: Java/StackedBarChart/StackedBarChart
date: 2021-01-04
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
* **ObservableList&lt;XYChart.Series&lt;X**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<XYChart.Series<X" %}
* **Axis&lt;X&gt; xAxis**,  {% include w3api/param_description.html metodo=_data parametro="Axis<X> xAxis" %}
* **Y&gt;&gt; data**,  {% include w3api/param_description.html metodo=_data parametro="Y>> data" %}
* **double categoryGap**,  {% include w3api/param_description.html metodo=_data parametro="double categoryGap" %}
* **Axis&lt;Y&gt; yAxis**,  {% include w3api/param_description.html metodo=_data parametro="Axis<Y> yAxis" %}

## Clase Padre
[StackedBarChart](/Java/StackedBarChart/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackedBarChart.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
