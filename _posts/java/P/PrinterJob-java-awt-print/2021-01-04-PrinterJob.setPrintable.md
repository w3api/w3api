---
title: PrinterJob.setPrintable()
permalink: Java/PrinterJob-java-awt-print/setPrintable
date: 2021-01-04
key: JavaJava.P.PrinterJob-java-awt-print
category: java
tags: ['java se', 'java.awt.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterJob-java-awt-print.metodos valor="setPrintable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setPrintable(Printable painter)
public abstract void setPrintable(Printable painter, PageFormat format)
~~~

## Parámetros
* **Printable painter**,  {% include w3api/param_description.html metodo=_data parametro="Printable painter" %}
* **PageFormat format**,  {% include w3api/param_description.html metodo=_data parametro="PageFormat format" %}

## Clase Padre
[PrinterJob](/Java/PrinterJob-java-awt-print/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrinterJob-java-awt-print.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
