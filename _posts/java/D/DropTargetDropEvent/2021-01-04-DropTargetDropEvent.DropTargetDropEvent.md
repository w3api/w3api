---
title: DropTargetDropEvent.DropTargetDropEvent()
permalink: Java/DropTargetDropEvent/DropTargetDropEvent
date: 2021-01-04
key: JavaJava.D.DropTargetDropEvent
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DropTargetDropEvent.constructores valor="DropTargetDropEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DropTargetDropEvent(DropTargetContext dtc, Point cursorLocn, int dropAction, int srcActions)
public DropTargetDropEvent(DropTargetContext dtc, Point cursorLocn, int dropAction, int srcActions, boolean isLocal)
~~~

## Parámetros
* **int srcActions**,  {% include w3api/param_description.html metodo=_data parametro="int srcActions" %}
* **DropTargetContext dtc**,  {% include w3api/param_description.html metodo=_data parametro="DropTargetContext dtc" %}
* **boolean isLocal**,  {% include w3api/param_description.html metodo=_data parametro="boolean isLocal" %}
* **int dropAction**,  {% include w3api/param_description.html metodo=_data parametro="int dropAction" %}
* **Point cursorLocn**,  {% include w3api/param_description.html metodo=_data parametro="Point cursorLocn" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DropTargetDropEvent](/Java/DropTargetDropEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DropTargetDropEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
