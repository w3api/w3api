---
title: DragSourceEvent.DragSourceEvent()
permalink: Java/DragSourceEvent/DragSourceEvent
date: 2021-01-11
key: JavaJava.D.DragSourceEvent
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSourceEvent.constructores valor="DragSourceEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragSourceEvent(DragSourceContext dsc)
public DragSourceEvent(DragSourceContext dsc, int x, int y)
~~~

## Parámetros
* **DragSourceContext dsc**,  {% include w3api/param_description.html metodo=_dato parametro="DragSourceContext dsc" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragSourceEvent](/Java/DragSourceEvent/)

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
