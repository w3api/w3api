---
title: PrinterStateReasons
permalink: /Java/PrinterStateReasons/
date: 2021-01-11
key: Java.P.PrinterStateReasons
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrinterStateReasons.description }}

## Sintaxis
~~~java
public final class PrinterStateReasons extends HashMap<PrinterStateReason,Severity> implements PrintServiceAttribute
~~~

## Constructores
* [PrinterStateReasons()](/Java/PrinterStateReasons/PrinterStateReasons/)

## Métodos
* [getCategory()](/Java/PrinterStateReasons/getCategory)
* [getName()](/Java/PrinterStateReasons/getName)
* [printerStateReasonSet()](/Java/PrinterStateReasons/printerStateReasonSet)
* [put()](/Java/PrinterStateReasons/put)

## Ejemplo
~~~java
{{ site.data.Java.P.PrinterStateReasons.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrinterStateReasons.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
