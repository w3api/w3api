---
title: PrintJobEvent
permalink: Java/PrintJobEvent
date: 2021-01-04
key: JavaJava.P.PrintJobEvent
category: java
tags: ['java se', 'javax.print.event', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrintJobEvent.description }}

## Sintaxis
~~~java
public class PrintJobEvent extends PrintEvent
~~~

## Constructores
* [PrintJobEvent()](/Java/PrintJobEvent/PrintJobEvent/)

## Campos
* [DATA_TRANSFER_COMPLETE](/Java/PrintJobEvent/DATA_TRANSFER_COMPLETE)
* [JOB_CANCELED](/Java/PrintJobEvent/JOB_CANCELED)
* [JOB_COMPLETE](/Java/PrintJobEvent/JOB_COMPLETE)
* [JOB_FAILED](/Java/PrintJobEvent/JOB_FAILED)
* [NO_MORE_EVENTS](/Java/PrintJobEvent/NO_MORE_EVENTS)
* [REQUIRES_ATTENTION](/Java/PrintJobEvent/REQUIRES_ATTENTION)

## Métodos
* [getPrintEventType()](/Java/PrintJobEvent/getPrintEventType)
* [getPrintJob()](/Java/PrintJobEvent/getPrintJob)

## Ejemplo
~~~java
{{ site.data.Java.P.PrintJobEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintJobEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
