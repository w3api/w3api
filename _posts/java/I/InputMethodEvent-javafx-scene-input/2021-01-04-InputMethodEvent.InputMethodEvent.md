---
title: InputMethodEvent.InputMethodEvent()
permalink: Java/InputMethodEvent-javafx-scene-input/InputMethodEvent
date: 2021-01-04
key: JavaJava.I.InputMethodEvent-javafx-scene-input
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethodEvent-javafx-scene-input.constructores valor="InputMethodEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputMethodEvent(Object source, EventTarget target, EventType<InputMethodEvent> eventType, List<InputMethodTextRun> composed, String committed, int caretPosition)
public InputMethodEvent(EventType<InputMethodEvent> eventType, List<InputMethodTextRun> composed, String committed, int caretPosition)
~~~

## Parámetros
* **List&lt;InputMethodTextRun&gt; composed**,  {% include w3api/param_description.html metodo=_data parametro="List<InputMethodTextRun> composed" %}
* **String committed**,  {% include w3api/param_description.html metodo=_data parametro="String committed" %}
* **int caretPosition**,  {% include w3api/param_description.html metodo=_data parametro="int caretPosition" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **EventType&lt;InputMethodEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<InputMethodEvent> eventType" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[InputMethodEvent](/Java/InputMethodEvent-javafx-scene-input/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputMethodEvent-javafx-scene-input.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
