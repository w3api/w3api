---
title: PrintJobEvent.PrintJobEvent()
permalink: /Java/PrintJobEvent/PrintJobEvent/
date: 2021-01-11
key: Java.P.PrintJobEvent
category: Java
tags: ['java se', 'javax.print.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintJobEvent.constructores valor="PrintJobEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintJobEvent(DocPrintJob source, int reason)
~~~

## Parámetros
* **DocPrintJob source**,  {% include w3api/param_description.html metodo=_dato parametro="DocPrintJob source" %}
* **int reason**,  {% include w3api/param_description.html metodo=_dato parametro="int reason" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintJobEvent](/Java/PrintJobEvent/)

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
