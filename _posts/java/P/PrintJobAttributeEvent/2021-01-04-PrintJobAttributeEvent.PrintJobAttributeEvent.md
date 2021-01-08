---
title: PrintJobAttributeEvent.PrintJobAttributeEvent()
permalink: Java/PrintJobAttributeEvent/PrintJobAttributeEvent
date: 2021-01-04
key: JavaJava.P.PrintJobAttributeEvent
category: java
tags: ['java se', 'javax.print.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintJobAttributeEvent.constructores valor="PrintJobAttributeEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintJobAttributeEvent(DocPrintJob source, PrintJobAttributeSet attributes)
~~~

## Parámetros
* **DocPrintJob source**,  {% include w3api/param_description.html metodo=_data parametro="DocPrintJob source" %}
* **PrintJobAttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="PrintJobAttributeSet attributes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintJobAttributeEvent](/Java/PrintJobAttributeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintJobAttributeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
