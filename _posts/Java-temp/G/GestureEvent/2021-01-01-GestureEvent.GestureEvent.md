---
title: GestureEvent.GestureEvent()
permalink: /Java/GestureEvent/GestureEvent/
date: 2021-01-11
key: Java.G.GestureEvent
category: Java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GestureEvent.constructores valor="GestureEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="8") protected GestureEvent(Object source, EventTarget target, EventType<? extends GestureEvent> eventType)
protected GestureEvent(Object source, EventTarget target, EventType<? extends GestureEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, PickResult pickResult)
@Deprecated(since="8") protected GestureEvent(EventType<? extends GestureEvent> eventType)
protected GestureEvent(EventType<? extends GestureEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, PickResult pickResult)
~~~

## Parámetros
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_dato parametro="boolean direct" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **EventType&lt;? extends GestureEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? extends GestureEvent> eventType" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inertia" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}

## Clase Padre
[GestureEvent](/Java/GestureEvent/)

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
