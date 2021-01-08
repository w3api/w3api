---
title: PaintEvent.PaintEvent()
permalink: Java/PaintEvent/PaintEvent
date: 2021-01-04
key: JavaJava.P.PaintEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PaintEvent.constructores valor="PaintEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PaintEvent(Component source, int id, Rectangle updateRect)
~~~

## Parámetros
* **Rectangle updateRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle updateRect" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PaintEvent](/Java/PaintEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PaintEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
