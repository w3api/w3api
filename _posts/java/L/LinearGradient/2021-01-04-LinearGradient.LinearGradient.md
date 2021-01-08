---
title: LinearGradient.LinearGradient()
permalink: Java/LinearGradient/LinearGradient
date: 2021-01-04
key: JavaJava.L.LinearGradient
category: java
tags: ['java se', 'javafx.scene.paint', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinearGradient.constructores valor="LinearGradient" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinearGradient(double startX, double startY, double endX, double endY, boolean proportional, CycleMethod cycleMethod, List<Stop> stops)
public LinearGradient(double startX, double startY, double endX, double endY, boolean proportional, CycleMethod cycleMethod, Stop... stops)
~~~

## Parámetros
* **double endY**,  {% include w3api/param_description.html metodo=_data parametro="double endY" %}
* **CycleMethod cycleMethod**,  {% include w3api/param_description.html metodo=_data parametro="CycleMethod cycleMethod" %}
* **Stop... stops**,  {% include w3api/param_description.html metodo=_data parametro="Stop... stops" %}
* **double startX**,  {% include w3api/param_description.html metodo=_data parametro="double startX" %}
* **List&lt;Stop&gt; stops**,  {% include w3api/param_description.html metodo=_data parametro="List<Stop> stops" %}
* **double endX**,  {% include w3api/param_description.html metodo=_data parametro="double endX" %}
* **double startY**,  {% include w3api/param_description.html metodo=_data parametro="double startY" %}
* **boolean proportional**,  {% include w3api/param_description.html metodo=_data parametro="boolean proportional" %}

## Clase Padre
[LinearGradient](/Java/LinearGradient/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinearGradient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
