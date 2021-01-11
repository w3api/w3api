---
title: PrintJobAdapter
permalink: Java/PrintJobAdapter
date: 2021-01-11
key: JavaJava.P.PrintJobAdapter
category: java
tags: ['java se', 'javax.print.event', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrintJobAdapter.description }}

## Sintaxis
~~~java
public abstract class PrintJobAdapter extends Object implements PrintJobListener
~~~

## Constructores
* [PrintJobAdapter()](/Java/PrintJobAdapter/PrintJobAdapter/)

## Métodos
* [printDataTransferCompleted()](/Java/PrintJobAdapter/printDataTransferCompleted)
* [printJobCanceled()](/Java/PrintJobAdapter/printJobCanceled)
* [printJobCompleted()](/Java/PrintJobAdapter/printJobCompleted)
* [printJobFailed()](/Java/PrintJobAdapter/printJobFailed)
* [printJobNoMoreEvents()](/Java/PrintJobAdapter/printJobNoMoreEvents)
* [printJobRequiresAttention()](/Java/PrintJobAdapter/printJobRequiresAttention)

## Ejemplo
~~~java
{{ site.data.Java.P.PrintJobAdapter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintJobAdapter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
