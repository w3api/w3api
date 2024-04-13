---
title: ValueAxis.autoRange()
permalink: /Java/ValueAxis/autoRange/
date: 2021-01-11
key: Java.V.ValueAxis
category: Java
tags: ['java se', 'javafx.scene.chart', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueAxis.metodos valor="autoRange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Object autoRange(double length)
protected Object autoRange(double minValue, double maxValue, double length, double labelSize)
~~~

## Parámetros
* **double minValue**,  {% include w3api/param_description.html metodo=_dato parametro="double minValue" %}
* **double labelSize**,  {% include w3api/param_description.html metodo=_dato parametro="double labelSize" %}
* **double length**,  {% include w3api/param_description.html metodo=_dato parametro="double length" %}
* **double maxValue**,  {% include w3api/param_description.html metodo=_dato parametro="double maxValue" %}

## Clase Padre
[ValueAxis](/Java/ValueAxis/)

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
