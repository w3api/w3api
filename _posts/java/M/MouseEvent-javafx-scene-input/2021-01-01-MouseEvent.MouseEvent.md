---
title: MouseEvent.MouseEvent()
permalink: Java/MouseEvent-javafx-scene-input/MouseEvent
date: 2021-01-11
key: JavaJava.M.MouseEvent-javafx-scene-input
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseEvent-javafx-scene-input.constructores valor="MouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MouseEvent(Object source, EventTarget target, EventType<? extends MouseEvent> eventType, double x, double y, double screenX, double screenY, MouseButton button, int clickCount, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean primaryButtonDown, boolean middleButtonDown, boolean secondaryButtonDown, boolean synthesized, boolean popupTrigger, boolean stillSincePress, PickResult pickResult)
public MouseEvent(EventType<? extends MouseEvent> eventType, double x, double y, double screenX, double screenY, MouseButton button, int clickCount, boolean shiftDown, boolean controlDown, boolean altDown, boolean metaDown, boolean primaryButtonDown, boolean middleButtonDown, boolean secondaryButtonDown, boolean synthesized, boolean popupTrigger, boolean stillSincePress, PickResult pickResult)
~~~

## Parámetros
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean controlDown" %}
* **boolean secondaryButtonDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean secondaryButtonDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **boolean synthesized**,  {% include w3api/param_description.html metodo=_dato parametro="boolean synthesized" %}
* **MouseButton button**,  {% include w3api/param_description.html metodo=_dato parametro="MouseButton button" %}
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftDown" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaDown" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_dato parametro="int clickCount" %}
* **boolean stillSincePress**,  {% include w3api/param_description.html metodo=_dato parametro="boolean stillSincePress" %}
* **boolean primaryButtonDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean primaryButtonDown" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_dato parametro="boolean popupTrigger" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}
* **boolean middleButtonDown**,  {% include w3api/param_description.html metodo=_dato parametro="boolean middleButtonDown" %}
* **EventType&lt;? extends MouseEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? extends MouseEvent> eventType" %}

## Clase Padre
[MouseEvent](/Java/MouseEvent-javafx-scene-input/)

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
