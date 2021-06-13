---
title: DragEvent.DragEvent()
permalink: /Java/DragEvent/DragEvent/
date: 2021-01-11
key: Java.D.DragEvent
category: Java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragEvent.constructores valor="DragEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragEvent(Object source, EventTarget target, EventType<DragEvent> eventType, Dragboard dragboard, double x, double y, double screenX, double screenY, TransferMode transferMode, Object gestureSource, Object gestureTarget, PickResult pickResult)
public DragEvent(EventType<DragEvent> eventType, Dragboard dragboard, double x, double y, double screenX, double screenY, TransferMode transferMode, Object gestureSource, Object gestureTarget, PickResult pickResult)
~~~

## Parámetros
* **Dragboard dragboard**,  {% include w3api/param_description.html metodo=_dato parametro="Dragboard dragboard" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **TransferMode transferMode**,  {% include w3api/param_description.html metodo=_dato parametro="TransferMode transferMode" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object gestureSource" %}
* **EventType&lt;DragEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<DragEvent> eventType" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **Object gestureTarget**,  {% include w3api/param_description.html metodo=_dato parametro="Object gestureTarget" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}

## Clase Padre
[DragEvent](/Java/DragEvent/)

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
