---
title: PrintJobListener
permalink: /Java/PrintJobListener/
date: 2021-01-11
key: Java.P.PrintJobListener
category: java
tags: ['java se', 'javax.print.event', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrintJobListener.description }}

## Sintaxis
~~~java
public interface PrintJobListener
~~~

## Métodos
* [printDataTransferCompleted()](/Java/PrintJobListener/printDataTransferCompleted)
* [printJobCanceled()](/Java/PrintJobListener/printJobCanceled)
* [printJobCompleted()](/Java/PrintJobListener/printJobCompleted)
* [printJobFailed()](/Java/PrintJobListener/printJobFailed)
* [printJobNoMoreEvents()](/Java/PrintJobListener/printJobNoMoreEvents)
* [printJobRequiresAttention()](/Java/PrintJobListener/printJobRequiresAttention)

## Ejemplo
~~~java
{{ site.data.Java.P.PrintJobListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintJobListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
