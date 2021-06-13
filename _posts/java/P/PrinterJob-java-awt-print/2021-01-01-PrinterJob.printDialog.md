---
title: PrinterJob.printDialog()
permalink: /Java/PrinterJob-java-awt-print/printDialog/
date: 2021-01-11
key: Java.P.PrinterJob-java-awt-print
category: java
tags: ['java se', 'java.awt.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterJob-java-awt-print.metodos valor="printDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean printDialog() throws HeadlessException
public boolean printDialog(PrintRequestAttributeSet attributes) throws HeadlessException
~~~

## Parámetros
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="PrintRequestAttributeSet attributes" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrinterJob](/Java/PrinterJob-java-awt-print/)

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
