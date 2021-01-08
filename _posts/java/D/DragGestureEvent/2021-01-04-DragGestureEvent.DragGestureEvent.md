---
title: DragGestureEvent.DragGestureEvent()
permalink: Java/DragGestureEvent/DragGestureEvent
date: 2021-01-04
key: JavaJava.D.DragGestureEvent
category: java
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
* **DragGestureRecognizer dgr**,  {% include w3api/param_description.html metodo=_data parametro="DragGestureRecognizer dgr" %}
* **int act**,  {% include w3api/param_description.html metodo=_data parametro="int act" %}
* **Point ori**,  {% include w3api/param_description.html metodo=_data parametro="Point ori" %}
* **List&lt;? extends InputEvent&gt; evs**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends InputEvent> evs" %}

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
{%- for _ldc in site.data.Java.D.DragGestureEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
