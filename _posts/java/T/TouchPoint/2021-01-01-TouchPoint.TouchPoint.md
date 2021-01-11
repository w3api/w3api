---
title: TouchPoint.TouchPoint()
permalink: Java/TouchPoint/TouchPoint
date: 2021-01-11
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
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **TouchPoint.State state**,  {% include w3api/param_description.html metodo=_dato parametro="TouchPoint.State state" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}

## Clase Padre
[TouchPoint](/Java/TouchPoint/)

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
