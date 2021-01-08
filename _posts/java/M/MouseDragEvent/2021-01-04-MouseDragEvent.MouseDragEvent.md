---
title: MouseDragEvent.MouseDragEvent()
permalink: Java/MouseDragEvent/MouseDragEvent
date: 2021-01-04
key: JavaJava.M.MouseDragEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseDragEvent.constructores valor="MouseDragEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MouseDragEvent(Object source, EventTarget target, EventType<MouseDragEvent> eventType, double x, double y, double screenX, double screenY, MouseButton button, int clickCount, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean primaryButtonDown, boolean middleButtonDown, boolean secondaryButtonDown, boolean synthesized, boolean popupTrigger, PickResult pickResult, Object gestureSource)
public MouseDragEvent(EventType<MouseDragEvent> eventType, double x, double y, double screenX, double screenY, MouseButton button, int clickCount, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean primaryButtonDown, boolean middleButtonDown, boolean secondaryButtonDown, boolean synthesized, boolean popupTrigger, PickResult pickResult, Object gestureSource)
~~~

## Parámetros
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_data parametro="Object gestureSource" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **boolean synthesized**,  {% include w3api/param_description.html metodo=_data parametro="boolean synthesized" %}
* **boolean secondaryButtonDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean secondaryButtonDown" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **boolean primaryButtonDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean primaryButtonDown" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **boolean middleButtonDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean middleButtonDown" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_data parametro="int clickCount" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **EventType&lt;MouseDragEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<MouseDragEvent> eventType" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **MouseButton button**,  {% include w3api/param_description.html metodo=_data parametro="MouseButton button" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_data parametro="boolean popupTrigger" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[MouseDragEvent](/Java/MouseDragEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MouseDragEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
