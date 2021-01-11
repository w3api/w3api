---
title: DragEvent.copyFor()
permalink: Java/DragEvent/copyFor
date: 2021-01-11
key: JavaJava.D.DragEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragEvent.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragEvent copyFor(Object source, EventTarget target, Object gestureSource, Object gestureTarget, EventType<DragEvent> eventType)
public DragEvent copyFor(Object source, EventTarget target, EventType<DragEvent> type)
~~~

## Parámetros
* **EventType&lt;DragEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<DragEvent> type" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object gestureSource" %}
* **EventType&lt;DragEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<DragEvent> eventType" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **Object gestureTarget**,  {% include w3api/param_description.html metodo=_dato parametro="Object gestureTarget" %}

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
