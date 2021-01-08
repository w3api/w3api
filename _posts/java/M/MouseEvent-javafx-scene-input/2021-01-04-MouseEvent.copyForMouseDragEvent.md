---
title: MouseEvent.copyForMouseDragEvent()
permalink: Java/MouseEvent-javafx-scene-input/copyForMouseDragEvent
date: 2021-01-04
key: JavaJava.M.MouseEvent-javafx-scene-input
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseEvent-javafx-scene-input.metodos valor="copyForMouseDragEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MouseDragEvent copyForMouseDragEvent(MouseEvent e, Object source, EventTarget target, EventType<MouseDragEvent> type, Object gestureSource, PickResult pickResult)
~~~

## Parámetros
* **MouseEvent e**,  {% include w3api/param_description.html metodo=_data parametro="MouseEvent e" %}
* **EventType&lt;MouseDragEvent&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="EventType<MouseDragEvent> type" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_data parametro="Object gestureSource" %}
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_data parametro="PickResult pickResult" %}
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
