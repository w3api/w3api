---
title: TouchEvent.TouchEvent()
permalink: Java/TouchEvent/TouchEvent
date: 2021-01-11
key: JavaJava.T.TouchEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TouchEvent.constructores valor="TouchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TouchEvent(Object source, EventTarget target, EventType<TouchEvent> eventType, TouchPoint touchPoint, List<TouchPoint> touchPoints, int eventSetId, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown)
public TouchEvent(EventType<TouchEvent> eventType, TouchPoint touchPoint, List<TouchPoint> touchPoints, int eventSetId, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown)
~~~

## Parámetros
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **EventType&lt;TouchEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<TouchEvent> eventType" %}
* **List&lt;TouchPoint&gt; touchPoints**,  {% include w3api/param_description.html metodo=_dato parametro="List<TouchPoint> touchPoints" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **TouchPoint touchPoint**,  {% include w3api/param_description.html metodo=_dato parametro="TouchPoint touchPoint" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **int eventSetId**,  {% include w3api/param_description.html metodo=_dato parametro="int eventSetId" %}

## Clase Padre
[TouchEvent](/Java/TouchEvent/)

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
