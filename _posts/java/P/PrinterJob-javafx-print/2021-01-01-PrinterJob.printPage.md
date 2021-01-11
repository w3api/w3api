---
title: PrinterJob.printPage()
permalink: Java/PrinterJob-javafx-print/printPage
date: 2021-01-11
key: JavaJava.P.PrinterJob-javafx-print
category: java
tags: ['java se', 'javafx.print', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterJob-javafx-print.metodos valor="printPage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean printPage(PageLayout pageLayout, Node node)
public boolean printPage(Node node)
~~~

## Parámetros
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}
* **PageLayout pageLayout**,  {% include w3api/param_description.html metodo=_dato parametro="PageLayout pageLayout" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrinterJob](/Java/PrinterJob-javafx-print/)

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
