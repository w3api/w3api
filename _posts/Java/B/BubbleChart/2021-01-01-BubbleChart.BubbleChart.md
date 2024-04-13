---
title: BubbleChart.BubbleChart()
permalink: /Java/BubbleChart/BubbleChart/
date: 2021-01-11
key: Java.B.BubbleChart
category: Java
tags: ['java se', 'javafx.scene.chart', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BubbleChart.constructores valor="BubbleChart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BubbleChart(Axis<X> xAxis, Axis<Y> yAxis)
public BubbleChart(Axis<X> xAxis, Axis<Y> yAxis, ObservableList<XYChart.Series<X,Y>> data)
~~~

## Parámetros
* **Axis&lt;Y&gt; yAxis**,  {% include w3api/param_description.html metodo=_dato parametro="Axis<Y> yAxis" %}
* **Y&gt;&gt; data**,  {% include w3api/param_description.html metodo=_dato parametro="Y>> data" %}
* **ObservableList&lt;XYChart.Series&lt;X**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<XYChart.Series<X" %}
* **Axis&lt;X&gt; xAxis**,  {% include w3api/param_description.html metodo=_dato parametro="Axis<X> xAxis" %}

## Clase Padre
[BubbleChart](/Java/BubbleChart/)

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
