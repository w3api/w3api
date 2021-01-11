---
title: Printable.print()
permalink: Java/Printable/print
date: 2021-01-11
key: JavaJava.P.Printable
category: java
tags: ['java se', 'java.awt.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Printable.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int print(Graphics graphics, PageFormat pageFormat, int pageIndex) throws PrinterException
~~~

## Parámetros
* **Graphics graphics**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics graphics" %}
* **int pageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int pageIndex" %}
* **PageFormat pageFormat**,  {% include w3api/param_description.html metodo=_dato parametro="PageFormat pageFormat" %}

## Excepciones
[PrinterException](/Java/PrinterException/)

## Clase Padre
[Printable](/Java/Printable/)

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
