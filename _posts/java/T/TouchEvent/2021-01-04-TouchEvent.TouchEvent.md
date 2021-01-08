---
title: TouchEvent.TouchEvent()
permalink: Java/TouchEvent/TouchEvent
date: 2021-01-04
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
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **int eventSetId**,  {% include w3api/param_description.html metodo=_data parametro="int eventSetId" %}
* **TouchPoint touchPoint**,  {% include w3api/param_description.html metodo=_data parametro="TouchPoint touchPoint" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **EventType&lt;TouchEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<TouchEvent> eventType" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **List&lt;TouchPoint&gt; touchPoints**,  {% include w3api/param_description.html metodo=_data parametro="List<TouchPoint> touchPoints" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[TouchEvent](/Java/TouchEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TouchEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
