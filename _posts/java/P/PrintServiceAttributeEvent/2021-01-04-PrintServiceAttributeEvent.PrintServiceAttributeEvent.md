---
title: PrintServiceAttributeEvent.PrintServiceAttributeEvent()
permalink: Java/PrintServiceAttributeEvent/PrintServiceAttributeEvent
date: 2021-01-04
key: JavaJava.P.PrintServiceAttributeEvent
category: java
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
* **PrintServiceAttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="PrintServiceAttributeSet attributes" %}
* **PrintService source**,  {% include w3api/param_description.html metodo=_data parametro="PrintService source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintServiceAttributeEvent](/Java/PrintServiceAttributeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintServiceAttributeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
