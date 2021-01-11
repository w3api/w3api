---
title: ZoomEvent.ZoomEvent()
permalink: Java/ZoomEvent/ZoomEvent
date: 2021-01-11
key: JavaJava.Z.ZoomEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoomEvent.constructores valor="ZoomEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZoomEvent(Object source, EventTarget target, EventType<ZoomEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double zoomFactor, double totalZoomFactor, PickResult pickResult)
public ZoomEvent(EventType<ZoomEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double zoomFactor, double totalZoomFactor, PickResult pickResult)
~~~

## Parámetros
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_dato parametro="boolean direct" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inertia" %}
* **EventType&lt;ZoomEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<ZoomEvent> eventType" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double totalZoomFactor**,  {% include w3api/param_description.html metodo=_dato parametro="double totalZoomFactor" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}
* **double zoomFactor**,  {% include w3api/param_description.html metodo=_dato parametro="double zoomFactor" %}

## Clase Padre
[ZoomEvent](/Java/ZoomEvent/)

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
