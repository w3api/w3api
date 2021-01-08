---
title: DragEvent.copyFor()
permalink: Java/DragEvent/copyFor
date: 2021-01-04
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
* **EventType&lt;DragEvent&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="EventType<DragEvent> type" %}
* **Object gestureTarget**,  {% include w3api/param_description.html metodo=_data parametro="Object gestureTarget" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **EventType&lt;DragEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<DragEvent> eventType" %}
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_data parametro="Object gestureSource" %}
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
