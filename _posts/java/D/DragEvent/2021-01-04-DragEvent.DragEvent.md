---
title: DragEvent.DragEvent()
permalink: Java/DragEvent/DragEvent
date: 2021-01-04
key: JavaJava.D.DragEvent
category: java
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
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **TransferMode transferMode**,  {% include w3api/param_description.html metodo=_data parametro="TransferMode transferMode" %}
* **Object gestureTarget**,  {% include w3api/param_description.html metodo=_data parametro="Object gestureTarget" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **EventType&lt;DragEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<DragEvent> eventType" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **Dragboard dragboard**,  {% include w3api/param_description.html metodo=_data parametro="Dragboard dragboard" %}
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_data parametro="Object gestureSource" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[DragEvent](/Java/DragEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
