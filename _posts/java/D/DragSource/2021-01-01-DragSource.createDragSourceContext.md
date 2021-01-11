---
title: DragSource.createDragSourceContext()
permalink: Java/DragSource/createDragSourceContext
date: 2021-01-11
key: JavaJava.D.DragSource
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSource.metodos valor="createDragSourceContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected DragSourceContext createDragSourceContext(DragGestureEvent dgl, Cursor dragCursor, Image dragImage, Point imageOffset, Transferable t, DragSourceListener dsl)
~~~

## Parámetros
* **Transferable t**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable t" %}
* **Image dragImage**,  {% include w3api/param_description.html metodo=_dato parametro="Image dragImage" %}
* **DragGestureEvent dgl**,  {% include w3api/param_description.html metodo=_dato parametro="DragGestureEvent dgl" %}
* **Cursor dragCursor**,  {% include w3api/param_description.html metodo=_dato parametro="Cursor dragCursor" %}
* **DragSourceListener dsl**,  {% include w3api/param_description.html metodo=_dato parametro="DragSourceListener dsl" %}
* **Point imageOffset**,  {% include w3api/param_description.html metodo=_dato parametro="Point imageOffset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
