---
title: StringMonitor
permalink: Java/StringMonitor
date: 2021-01-11
key: JavaJava.S.StringMonitor
category: java
tags: ['java se', 'javax.management.monitor', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StringMonitor.description }}

## Sintaxis
~~~java
public class StringMonitor extends Monitor implements StringMonitorMBean
~~~

## Constructores
* [StringMonitor()](/Java/StringMonitor/StringMonitor/)

## Métodos
* [getDerivedGauge()](/Java/StringMonitor/getDerivedGauge)
* [getDerivedGaugeTimeStamp()](/Java/StringMonitor/getDerivedGaugeTimeStamp)
* [getNotificationInfo()](/Java/StringMonitor/getNotificationInfo)
* [getNotifyDiffer()](/Java/StringMonitor/getNotifyDiffer)
* [getNotifyMatch()](/Java/StringMonitor/getNotifyMatch)
* [getStringToCompare()](/Java/StringMonitor/getStringToCompare)
* [setNotifyDiffer()](/Java/StringMonitor/setNotifyDiffer)
* [setNotifyMatch()](/Java/StringMonitor/setNotifyMatch)
* [setStringToCompare()](/Java/StringMonitor/setStringToCompare)
* [start()](/Java/StringMonitor/start)
* [stop()](/Java/StringMonitor/stop)

## Ejemplo
~~~java
{{ site.data.Java.S.StringMonitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringMonitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
