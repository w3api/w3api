---
title: DropTargetDragEvent.DropTargetDragEvent()
permalink: Java/DropTargetDragEvent/DropTargetDragEvent
date: 2021-01-04
key: JavaJava.D.DropTargetDragEvent
category: java
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
* **int srcActions**,  {% include w3api/param_description.html metodo=_data parametro="int srcActions" %}
* **Point cursorLocn**,  {% include w3api/param_description.html metodo=_data parametro="Point cursorLocn" %}
* **DropTargetContext dtc**,  {% include w3api/param_description.html metodo=_data parametro="DropTargetContext dtc" %}
* **int dropAction**,  {% include w3api/param_description.html metodo=_data parametro="int dropAction" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DropTargetDragEvent](/Java/DropTargetDragEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DropTargetDragEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
