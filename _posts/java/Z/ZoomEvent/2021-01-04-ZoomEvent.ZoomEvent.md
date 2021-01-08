---
title: ZoomEvent.ZoomEvent()
permalink: Java/ZoomEvent/ZoomEvent
date: 2021-01-04
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
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_data parametro="boolean direct" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **EventType&lt;ZoomEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<ZoomEvent> eventType" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_data parametro="boolean inertia" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **double zoomFactor**,  {% include w3api/param_description.html metodo=_data parametro="double zoomFactor" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **double totalZoomFactor**,  {% include w3api/param_description.html metodo=_data parametro="double totalZoomFactor" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[ZoomEvent](/Java/ZoomEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Z.ZoomEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
