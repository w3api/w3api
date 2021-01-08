---
title: TouchPoint.TouchPoint()
permalink: Java/TouchPoint/TouchPoint
date: 2021-01-04
key: JavaJava.T.TouchPoint
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TouchPoint.constructores valor="TouchPoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TouchPoint(int id, TouchPoint.State state, double x, double y, double screenX, double screenY, EventTarget target, PickResult pickResult)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **TouchPoint.State state**,  {% include w3api/param_description.html metodo=_data parametro="TouchPoint.State state" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[TouchPoint](/Java/TouchPoint/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TouchPoint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
