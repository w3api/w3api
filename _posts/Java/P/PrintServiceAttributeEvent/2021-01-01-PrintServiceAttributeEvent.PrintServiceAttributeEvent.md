---
title: PrintServiceAttributeEvent.PrintServiceAttributeEvent()
permalink: /Java/PrintServiceAttributeEvent/PrintServiceAttributeEvent/
date: 2021-01-11
key: Java.P.PrintServiceAttributeEvent
category: Java
tags: ['java se', 'javax.print.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintServiceAttributeEvent.constructores valor="PrintServiceAttributeEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintServiceAttributeEvent(PrintService source, PrintServiceAttributeSet attributes)
~~~

## Parámetros
* **PrintService source**,  {% include w3api/param_description.html metodo=_dato parametro="PrintService source" %}
* **PrintServiceAttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="PrintServiceAttributeSet attributes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintServiceAttributeEvent](/Java/PrintServiceAttributeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
