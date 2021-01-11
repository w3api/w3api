---
title: ScrollEvent.ScrollEvent()
permalink: Java/ScrollEvent/ScrollEvent
date: 2021-01-11
key: JavaJava.S.ScrollEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScrollEvent.constructores valor="ScrollEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScrollEvent(Object source, EventTarget target, EventType<ScrollEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double deltaX, double deltaY, double totalDeltaX, double totalDeltaY, ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits, double textDeltaX, ScrollEvent.VerticalTextScrollUnits textDeltaYUnits, double textDeltaY, int touchCount, PickResult pickResult)
public ScrollEvent(EventType<ScrollEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double deltaX, double deltaY, double totalDeltaX, double totalDeltaY, double multiplierX, double multiplierY, ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits, double textDeltaX, ScrollEvent.VerticalTextScrollUnits textDeltaYUnits, double textDeltaY, int touchCount, PickResult pickResult)
public ScrollEvent(EventType<ScrollEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double deltaX, double deltaY, double totalDeltaX, double totalDeltaY, ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits, double textDeltaX, ScrollEvent.VerticalTextScrollUnits textDeltaYUnits, double textDeltaY, int touchCount, PickResult pickResult)
~~~

## Parámetros
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_dato parametro="boolean direct" %}
* **double totalDeltaX**,  {% include w3api/param_description.html metodo=_dato parametro="double totalDeltaX" %}
* **double textDeltaY**,  {% include w3api/param_description.html metodo=_dato parametro="double textDeltaY" %}
* **ScrollEvent.VerticalTextScrollUnits textDeltaYUnits**,  {% include w3api/param_description.html metodo=_dato parametro="ScrollEvent.VerticalTextScrollUnits textDeltaYUnits" %}
* **double totalDeltaY**,  {% include w3api/param_description.html metodo=_dato parametro="double totalDeltaY" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **int touchCount**,  {% include w3api/param_description.html metodo=_dato parametro="int touchCount" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inertia" %}
* **EventType&lt;ScrollEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<ScrollEvent> eventType" %}
* **ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits**,  {% include w3api/param_description.html metodo=_dato parametro="ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits" %}
* **double deltaY**,  {% include w3api/param_description.html metodo=_dato parametro="double deltaY" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}
* **double multiplierX**,  {% include w3api/param_description.html metodo=_dato parametro="double multiplierX" %}
* **double multiplierY**,  {% include w3api/param_description.html metodo=_dato parametro="double multiplierY" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double textDeltaX**,  {% include w3api/param_description.html metodo=_dato parametro="double textDeltaX" %}
* **double deltaX**,  {% include w3api/param_description.html metodo=_dato parametro="double deltaX" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}

## Clase Padre
[ScrollEvent](/Java/ScrollEvent/)

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
