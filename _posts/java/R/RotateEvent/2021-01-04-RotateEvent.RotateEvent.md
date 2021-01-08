---
title: RotateEvent.RotateEvent()
permalink: Java/RotateEvent/RotateEvent
date: 2021-01-04
key: JavaJava.R.RotateEvent
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
* **double angle**,  {% include w3api/param_description.html metodo=_data parametro="double angle" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **EventType&lt;RotateEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<RotateEvent> eventType" %}
* **boolean direct**,  {% include w3api/param_description.html metodo=_data parametro="boolean direct" %}
* **double totalAngle**,  {% include w3api/param_description.html metodo=_data parametro="double totalAngle" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **boolean inertia**,  {% include w3api/param_description.html metodo=_data parametro="boolean inertia" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[RotateEvent](/Java/RotateEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RotateEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
