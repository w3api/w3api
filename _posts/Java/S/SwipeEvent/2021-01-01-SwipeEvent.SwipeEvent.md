---
title: SwipeEvent.SwipeEvent()
permalink: /Java/SwipeEvent/SwipeEvent/
date: 2021-01-11
key: Java.S.SwipeEvent
category: Java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwipeEvent.constructores valor="SwipeEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SwipeEvent(Object source, EventTarget target, EventType<SwipeEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, int touchCount, PickResult pickResult)
public SwipeEvent(EventType<SwipeEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, int touchCount, PickResult pickResult)
~~~

## Parámetros
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **EventType&lt;SwipeEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<SwipeEvent> eventType" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_dato parametro="boolean direct" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **int touchCount**,  {% include w3api/param_description.html metodo=_dato parametro="int touchCount" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}

## Clase Padre
[SwipeEvent](/Java/SwipeEvent/)

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
