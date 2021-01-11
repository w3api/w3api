---
title: EventDispatcher.dispatchEvent()
permalink: Java/EventDispatcher/dispatchEvent
date: 2021-01-11
key: JavaJava.E.EventDispatcher
category: java
tags: ['java se', 'javafx.event', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventDispatcher.metodos valor="dispatchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Event dispatchEvent(Event event, EventDispatchChain tail)
~~~

## Parámetros
* **EventDispatchChain tail**,  {% include w3api/param_description.html metodo=_dato parametro="EventDispatchChain tail" %}
* **Event event**,  {% include w3api/param_description.html metodo=_dato parametro="Event event" %}

## Clase Padre
[EventDispatcher](/Java/EventDispatcher/)

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
