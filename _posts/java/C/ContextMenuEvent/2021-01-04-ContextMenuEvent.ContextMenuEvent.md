---
title: ContextMenuEvent.ContextMenuEvent()
permalink: Java/ContextMenuEvent/ContextMenuEvent
date: 2021-01-04
key: JavaJava.C.ContextMenuEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContextMenuEvent.constructores valor="ContextMenuEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ContextMenuEvent(Object source, EventTarget target, EventType<ContextMenuEvent> eventType, double x, double y, double screenX, double screenY, boolean keyboardTrigger, PickResult pickResult)
public ContextMenuEvent(EventType<ContextMenuEvent> eventType, double x, double y, double screenX, double screenY, boolean keyboardTrigger, PickResult pickResult)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **boolean keyboardTrigger**,  {% include w3api/param_description.html metodo=_data parametro="boolean keyboardTrigger" %}
* **EventType&lt;ContextMenuEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<ContextMenuEvent> eventType" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[ContextMenuEvent](/Java/ContextMenuEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ContextMenuEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
