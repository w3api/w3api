---
title: InputEvent.InputEvent()
permalink: Java/InputEvent-javafx-scene-input/InputEvent
date: 2021-01-11
key: JavaJava.I.InputEvent-javafx-scene-input
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputEvent-javafx-scene-input.constructores valor="InputEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputEvent(Object source, EventTarget target, EventType<? extends InputEvent> eventType)
public InputEvent(EventType<? extends InputEvent> eventType)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **EventType&lt;? extends InputEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? extends InputEvent> eventType" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}

## Clase Padre
[InputEvent](/Java/InputEvent-javafx-scene-input/)

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
