---
title: ScrollEvent.ScrollEvent()
permalink: Java/ScrollEvent/ScrollEvent
date: 2021-01-04
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
* **double deltaX**,  {% include w3api/param_description.html metodo=_data parametro="double deltaX" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **double textDeltaY**,  {% include w3api/param_description.html metodo=_data parametro="double textDeltaY" %}
* **EventType&lt;ScrollEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<ScrollEvent> eventType" %}
* **double textDeltaX**,  {% include w3api/param_description.html metodo=_data parametro="double textDeltaX" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_data parametro="boolean direct" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **double multiplierY**,  {% include w3api/param_description.html metodo=_data parametro="double multiplierY" %}
* **double deltaY**,  {% include w3api/param_description.html metodo=_data parametro="double deltaY" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **int touchCount**,  {% include w3api/param_description.html metodo=_data parametro="int touchCount" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **double totalDeltaY**,  {% include w3api/param_description.html metodo=_data parametro="double totalDeltaY" %}
* **ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits**,  {% include w3api/param_description.html metodo=_data parametro="ScrollEvent.HorizontalTextScrollUnits textDeltaXUnits" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **double totalDeltaX**,  {% include w3api/param_description.html metodo=_data parametro="double totalDeltaX" %}
* **double multiplierX**,  {% include w3api/param_description.html metodo=_data parametro="double multiplierX" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_data parametro="boolean inertia" %}
* **ScrollEvent.VerticalTextScrollUnits textDeltaYUnits**,  {% include w3api/param_description.html metodo=_data parametro="ScrollEvent.VerticalTextScrollUnits textDeltaYUnits" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}

## Clase Padre
[ScrollEvent](/Java/ScrollEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScrollEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
