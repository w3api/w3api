---
title: DragGestureEvent.DragGestureEvent()
permalink: /Java/DragGestureEvent/DragGestureEvent/
date: 2021-01-11
key: Java.D.DragGestureEvent
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragGestureEvent.constructores valor="DragGestureEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragGestureEvent(DragGestureRecognizer dgr, int act, Point ori, List<? extends InputEvent> evs)
~~~

## Parámetros
* **DragGestureRecognizer dgr**,  {% include w3api/param_description.html metodo=_dato parametro="DragGestureRecognizer dgr" %}
* **List&lt;? extends InputEvent&gt; evs**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends InputEvent> evs" %}
* **Point ori**,  {% include w3api/param_description.html metodo=_dato parametro="Point ori" %}
* **int act**,  {% include w3api/param_description.html metodo=_dato parametro="int act" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragGestureEvent](/Java/DragGestureEvent/)

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
