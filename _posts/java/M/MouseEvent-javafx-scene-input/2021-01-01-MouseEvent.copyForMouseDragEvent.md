---
title: MouseEvent.copyForMouseDragEvent()
permalink: Java/MouseEvent-javafx-scene-input/copyForMouseDragEvent
date: 2021-01-11
key: JavaJava.M.MouseEvent-javafx-scene-input
category: Java
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
* **PickResult pickResult**,  {% include w3api/param_description.html metodo=_dato parametro="PickResult pickResult" %}
* **MouseEvent e**,  {% include w3api/param_description.html metodo=_dato parametro="MouseEvent e" %}
* **EventType&lt;MouseDragEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<MouseDragEvent> type" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **Object gestureSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object gestureSource" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}

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
