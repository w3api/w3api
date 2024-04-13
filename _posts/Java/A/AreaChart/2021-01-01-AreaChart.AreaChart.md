---
title: AreaChart.AreaChart()
permalink: /Java/AreaChart/AreaChart/
date: 2021-01-11
key: Java.A.AreaChart
category: Java
tags: ['java se', 'javafx.scene.chart', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AreaChart.constructores valor="AreaChart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AreaChart(Axis<X> xAxis, Axis<Y> yAxis)
public AreaChart(Axis<X> xAxis, Axis<Y> yAxis, ObservableList<XYChart.Series<X,Y>> data)
~~~

## Parámetros
* **Axis&lt;Y&gt; yAxis**,  {% include w3api/param_description.html metodo=_dato parametro="Axis<Y> yAxis" %}
* **Y&gt;&gt; data**,  {% include w3api/param_description.html metodo=_dato parametro="Y>> data" %}
* **ObservableList&lt;XYChart.Series&lt;X**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<XYChart.Series<X" %}
* **Axis&lt;X&gt; xAxis**,  {% include w3api/param_description.html metodo=_dato parametro="Axis<X> xAxis" %}

## Clase Padre
[AreaChart](/Java/AreaChart/)

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
