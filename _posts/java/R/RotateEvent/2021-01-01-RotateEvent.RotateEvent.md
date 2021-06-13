---
title: RotateEvent.RotateEvent()
permalink: Java/RotateEvent/RotateEvent
date: 2021-01-11
key: Java.R.RotateEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RotateEvent.constructores valor="RotateEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RotateEvent(Object source, EventTarget target, EventType<RotateEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double angle, double totalAngle, PickResult pickResult)
public RotateEvent(EventType<RotateEvent> eventType, double x, double y, double screenX, double screenY, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean direct, boolean inertia, double angle, double totalAngle, PickResult pickResult)
~~~

## Parámetros
* **EventType&lt;RotateEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<RotateEvent> eventType" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **double totalAngle**,  {% include w3api/param_description.html metodo=_dato parametro="double totalAngle" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_dato parametro="boolean direct" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inertia" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}
* **double angle**,  {% include w3api/param_description.html metodo=_dato parametro="double angle" %}

## Clase Padre
[RotateEvent](/Java/RotateEvent/)

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
