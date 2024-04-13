---
title: DropTargetDragEvent.DropTargetDragEvent()
permalink: /Java/DropTargetDragEvent/DropTargetDragEvent/
date: 2021-01-11
key: Java.D.DropTargetDragEvent
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DropTargetDragEvent.constructores valor="DropTargetDragEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DropTargetDragEvent(DropTargetContext dtc, Point cursorLocn, int dropAction, int srcActions)
~~~

## Parámetros
* **int dropAction**,  {% include w3api/param_description.html metodo=_dato parametro="int dropAction" %}
* **int srcActions**,  {% include w3api/param_description.html metodo=_dato parametro="int srcActions" %}
* **Point cursorLocn**,  {% include w3api/param_description.html metodo=_dato parametro="Point cursorLocn" %}
* **DropTargetContext dtc**,  {% include w3api/param_description.html metodo=_dato parametro="DropTargetContext dtc" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DropTargetDragEvent](/Java/DropTargetDragEvent/)

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
