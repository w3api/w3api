---
title: DragGestureEvent.startDrag()
permalink: Java/DragGestureEvent/startDrag
date: 2021-01-11
key: JavaJava.D.DragGestureEvent
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragGestureEvent.metodos valor="startDrag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void startDrag(Cursor dragCursor, Transferable transferable) throws InvalidDnDOperationException
public void startDrag(Cursor dragCursor, Transferable transferable, DragSourceListener dsl) throws InvalidDnDOperationException
public void startDrag(Cursor dragCursor, Image dragImage, Point imageOffset, Transferable transferable, DragSourceListener dsl) throws InvalidDnDOperationException
~~~

## Parámetros
* **Transferable transferable**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable transferable" %}
* **Image dragImage**,  {% include w3api/param_description.html metodo=_dato parametro="Image dragImage" %}
* **Cursor dragCursor**,  {% include w3api/param_description.html metodo=_dato parametro="Cursor dragCursor" %}
* **DragSourceListener dsl**,  {% include w3api/param_description.html metodo=_dato parametro="DragSourceListener dsl" %}
* **Point imageOffset**,  {% include w3api/param_description.html metodo=_dato parametro="Point imageOffset" %}

## Excepciones
[InvalidDnDOperationException](/Java/InvalidDnDOperationException/), [NullPointerException](/Java/NullPointerException/)

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
