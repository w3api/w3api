---
title: WindowEvent.WindowEvent()
permalink: Java/WindowEvent-javafx-stage/WindowEvent
date: 2021-01-11
key: JavaJava.W.WindowEvent-javafx-stage
category: java
tags: ['java se', 'javafx.stage', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WindowEvent-javafx-stage.constructores valor="WindowEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WindowEvent(Window source, EventType<? extends Event> eventType)
~~~

## Parámetros
* **EventType&lt;? extends Event&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? extends Event> eventType" %}
* **Window source**,  {% include w3api/param_description.html metodo=_dato parametro="Window source" %}

## Clase Padre
[WindowEvent](/Java/WindowEvent-javafx-stage/)

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
