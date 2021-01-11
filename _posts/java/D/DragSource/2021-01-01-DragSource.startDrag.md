---
title: DragSource.startDrag()
permalink: Java/DragSource/startDrag
date: 2021-01-11
key: JavaJava.D.DragSource
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSource.metodos valor="startDrag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void startDrag(DragGestureEvent trigger, Cursor dragCursor, Transferable transferable, DragSourceListener dsl) throws InvalidDnDOperationException
public void startDrag(DragGestureEvent trigger, Cursor dragCursor, Transferable transferable, DragSourceListener dsl, FlavorMap flavorMap) throws InvalidDnDOperationException
public void startDrag(DragGestureEvent trigger, Cursor dragCursor, Image dragImage, Point dragOffset, Transferable transferable, DragSourceListener dsl) throws InvalidDnDOperationException
public void startDrag(DragGestureEvent trigger, Cursor dragCursor, Image dragImage, Point imageOffset, Transferable transferable, DragSourceListener dsl, FlavorMap flavorMap) throws InvalidDnDOperationException
~~~

## Parámetros
* **Transferable transferable**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable transferable" %}
* **FlavorMap flavorMap**,  {% include w3api/param_description.html metodo=_dato parametro="FlavorMap flavorMap" %}
* **Image dragImage**,  {% include w3api/param_description.html metodo=_dato parametro="Image dragImage" %}
* **Point dragOffset**,  {% include w3api/param_description.html metodo=_dato parametro="Point dragOffset" %}
* **DragGestureEvent trigger**,  {% include w3api/param_description.html metodo=_dato parametro="DragGestureEvent trigger" %}
* **Cursor dragCursor**,  {% include w3api/param_description.html metodo=_dato parametro="Cursor dragCursor" %}
* **DragSourceListener dsl**,  {% include w3api/param_description.html metodo=_dato parametro="DragSourceListener dsl" %}
* **Point imageOffset**,  {% include w3api/param_description.html metodo=_dato parametro="Point imageOffset" %}

## Excepciones
[InvalidDnDOperationException](/Java/InvalidDnDOperationException/)

## Clase Padre
[DragSource](/Java/DragSource/)

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
