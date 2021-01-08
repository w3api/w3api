---
title: MouseEvent.MouseEvent()
permalink: Java/MouseEvent-javafx-scene-input/MouseEvent
date: 2021-01-04
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
* **boolean shiftDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftDown" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **boolean synthesized**,  {% include w3api/param_description.html metodo=_data parametro="boolean synthesized" %}
* **EventType&lt;? extends MouseEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<? extends MouseEvent> eventType" %}
* **boolean secondaryButtonDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean secondaryButtonDown" %}
* **boolean altDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean altDown" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **boolean primaryButtonDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean primaryButtonDown" %}
* **boolean controlDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean controlDown" %}
* **boolean middleButtonDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean middleButtonDown" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_data parametro="int clickCount" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **MouseButton button**,  {% include w3api/param_description.html metodo=_data parametro="MouseButton button" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}
* **boolean stillSincePress**,  {% include w3api/param_description.html metodo=_data parametro="boolean stillSincePress" %}
* **boolean metaDown**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaDown" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_data parametro="boolean popupTrigger" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[MouseEvent](/Java/MouseEvent-javafx-scene-input/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MouseEvent-javafx-scene-input.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
