---
title: ContextMenuEvent.ContextMenuEvent()
permalink: /Java/ContextMenuEvent/ContextMenuEvent/
date: 2021-01-11
key: Java.C.ContextMenuEvent
category: Java
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
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **EventType&lt;ContextMenuEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<ContextMenuEvent> eventType" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}
* **boolean keyboardTrigger**,  {% include w3api/param_description.html metodo=_dato parametro="boolean keyboardTrigger" %}

## Clase Padre
[ContextMenuEvent](/Java/ContextMenuEvent/)

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
