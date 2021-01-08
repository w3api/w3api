---
title: DragSourceContext.DragSourceContext()
permalink: Java/DragSourceContext/DragSourceContext
date: 2021-01-04
key: JavaJava.D.DragSourceContext
category: java
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
* **DragGestureEvent trigger**,  {% include w3api/param_description.html metodo=_data parametro="DragGestureEvent trigger" %}
* **Cursor dragCursor**,  {% include w3api/param_description.html metodo=_data parametro="Cursor dragCursor" %}
* **Point offset**,  {% include w3api/param_description.html metodo=_data parametro="Point offset" %}
* **DragSourceListener dsl**,  {% include w3api/param_description.html metodo=_data parametro="DragSourceListener dsl" %}
* **Image dragImage**,  {% include w3api/param_description.html metodo=_data parametro="Image dragImage" %}
* **Transferable t**,  {% include w3api/param_description.html metodo=_data parametro="Transferable t" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragSourceContext](/Java/DragSourceContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSourceContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
