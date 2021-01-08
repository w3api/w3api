---
title: SwipeEvent.SwipeEvent()
permalink: Java/SwipeEvent/SwipeEvent
date: 2021-01-04
key: JavaJava.S.SwipeEvent
category: java
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
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_data parametro="boolean direct" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **EventType&lt;SwipeEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<SwipeEvent> eventType" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **int touchCount**,  {% include w3api/param_description.html metodo=_data parametro="int touchCount" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[SwipeEvent](/Java/SwipeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SwipeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
