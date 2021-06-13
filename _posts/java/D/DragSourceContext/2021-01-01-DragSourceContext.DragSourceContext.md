---
title: DragSourceContext.DragSourceContext()
permalink: /Java/DragSourceContext/DragSourceContext/
date: 2021-01-11
key: Java.D.DragSourceContext
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSourceContext.constructores valor="DragSourceContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragSourceContext(DragGestureEvent trigger, Cursor dragCursor, Image dragImage, Point offset, Transferable t, DragSourceListener dsl)
~~~

## Parámetros
* **Transferable t**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable t" %}
* **Image dragImage**,  {% include w3api/param_description.html metodo=_dato parametro="Image dragImage" %}
* **Point offset**,  {% include w3api/param_description.html metodo=_dato parametro="Point offset" %}
* **DragGestureEvent trigger**,  {% include w3api/param_description.html metodo=_dato parametro="DragGestureEvent trigger" %}
* **Cursor dragCursor**,  {% include w3api/param_description.html metodo=_dato parametro="Cursor dragCursor" %}
* **DragSourceListener dsl**,  {% include w3api/param_description.html metodo=_dato parametro="DragSourceListener dsl" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DragSourceContext](/Java/DragSourceContext/)

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
