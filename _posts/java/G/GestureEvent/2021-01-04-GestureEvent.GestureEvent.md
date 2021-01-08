---
title: GestureEvent.GestureEvent()
permalink: Java/GestureEvent/GestureEvent
date: 2021-01-04
key: JavaJava.G.GestureEvent
category: java
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
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_data parametro="boolean direct" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_data parametro="boolean inertia" %}
* **EventType&lt;? extends GestureEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<? extends GestureEvent> eventType" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[GestureEvent](/Java/GestureEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GestureEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
