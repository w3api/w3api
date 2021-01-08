---
title: DragSourceDropEvent.DragSourceDropEvent()
permalink: Java/DragSourceDropEvent/DragSourceDropEvent
date: 2021-01-04
key: JavaJava.D.DragSourceDropEvent
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSourceDropEvent.constructores valor="DragSourceDropEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragSourceDropEvent(DragSourceContext dsc)
public DragSourceDropEvent(DragSourceContext dsc, int action, boolean success)
public DragSourceDropEvent(DragSourceContext dsc, int action, boolean success, int x, int y)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int action**,  {% include w3api/param_description.html metodo=_data parametro="int action" %}
* **boolean success**,  {% include w3api/param_description.html metodo=_data parametro="boolean success" %}
* **DragSourceContext dsc**,  {% include w3api/param_description.html metodo=_data parametro="DragSourceContext dsc" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragSourceDropEvent](/Java/DragSourceDropEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSourceDropEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
