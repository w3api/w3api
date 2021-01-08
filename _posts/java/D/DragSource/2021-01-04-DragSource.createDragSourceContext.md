---
title: DragSource.createDragSourceContext()
permalink: Java/DragSource/createDragSourceContext
date: 2021-01-04
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
* **DragGestureEvent dgl**,  {% include w3api/param_description.html metodo=_data parametro="DragGestureEvent dgl" %}
* **Cursor dragCursor**,  {% include w3api/param_description.html metodo=_data parametro="Cursor dragCursor" %}
* **Point imageOffset**,  {% include w3api/param_description.html metodo=_data parametro="Point imageOffset" %}
* **DragSourceListener dsl**,  {% include w3api/param_description.html metodo=_data parametro="DragSourceListener dsl" %}
* **Image dragImage**,  {% include w3api/param_description.html metodo=_data parametro="Image dragImage" %}
* **Transferable t**,  {% include w3api/param_description.html metodo=_data parametro="Transferable t" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragSource](/Java/DragSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
