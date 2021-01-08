---
title: DragSourceDragEvent.DragSourceDragEvent()
permalink: Java/DragSourceDragEvent/DragSourceDragEvent
date: 2021-01-04
key: JavaJava.D.DragSourceDragEvent
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSourceDragEvent.constructores valor="DragSourceDragEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragSourceDragEvent(DragSourceContext dsc, int dropAction, int action, int modifiers)
public DragSourceDragEvent(DragSourceContext dsc, int dropAction, int action, int modifiers, int x, int y)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int action**,  {% include w3api/param_description.html metodo=_data parametro="int action" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **int dropAction**,  {% include w3api/param_description.html metodo=_data parametro="int dropAction" %}
* **DragSourceContext dsc**,  {% include w3api/param_description.html metodo=_data parametro="DragSourceContext dsc" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragSourceDragEvent](/Java/DragSourceDragEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSourceDragEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
