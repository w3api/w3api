---
title: PrintJobEvent.PrintJobEvent()
permalink: Java/PrintJobEvent/PrintJobEvent
date: 2021-01-04
key: JavaJava.P.PrintJobEvent
category: java
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
* **int reason**,  {% include w3api/param_description.html metodo=_data parametro="int reason" %}
* **DocPrintJob source**,  {% include w3api/param_description.html metodo=_data parametro="DocPrintJob source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintJobEvent](/Java/PrintJobEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintJobEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
