---
title: StackedAreaChart.StackedAreaChart()
permalink: Java/StackedAreaChart/StackedAreaChart
date: 2021-01-04
key: JavaJava.S.StackedAreaChart
category: java
tags: ['java se', 'javafx.scene.chart', 'javafx.controls', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackedAreaChart.constructores valor="StackedAreaChart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StackedAreaChart(Axis<X> xAxis, Axis<Y> yAxis)
public StackedAreaChart(Axis<X> xAxis, Axis<Y> yAxis, ObservableList<XYChart.Series<X,Y>> data)
~~~

## Parámetros
* **Axis&lt;Y&gt; yAxis**,  {% include w3api/param_description.html metodo=_data parametro="Axis<Y> yAxis" %}
* **Axis&lt;X&gt; xAxis**,  {% include w3api/param_description.html metodo=_data parametro="Axis<X> xAxis" %}
* **Y&gt;&gt; data**,  {% include w3api/param_description.html metodo=_data parametro="Y>> data" %}
* **ObservableList&lt;XYChart.Series&lt;X**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<XYChart.Series<X" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StackedAreaChart](/Java/StackedAreaChart/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackedAreaChart.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
