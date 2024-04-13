---
title: PrinterJob.setPrintService()
permalink: /Java/PrinterJob-java-awt-print/setPrintService/
date: 2021-01-11
key: Java.P.PrinterJob-java-awt-print
category: Java
tags: ['java se', 'java.awt.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterJob-java-awt-print.metodos valor="setPrintService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPrintService(PrintService service) throws PrinterException
~~~

## Parámetros
* **PrintService service**,  {% include w3api/param_description.html metodo=_dato parametro="PrintService service" %}

## Excepciones
[PrinterException](/Java/PrinterException/)

## Clase Padre
[PrinterJob](/Java/PrinterJob-java-awt-print/)

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
