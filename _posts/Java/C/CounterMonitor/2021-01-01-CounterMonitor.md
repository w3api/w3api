---
title: CounterMonitor
permalink: /Java/CounterMonitor/
date: 2021-01-11
key: Java.C.CounterMonitor
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CounterMonitor.description }}

## Sintaxis
~~~java
public class CounterMonitor extends Monitor implements CounterMonitorMBean
~~~

## Constructores
* [CounterMonitor()](/Java/CounterMonitor/CounterMonitor/)

## Métodos
* [getDerivedGauge()](/Java/CounterMonitor/getDerivedGauge)
* [getDerivedGaugeTimeStamp()](/Java/CounterMonitor/getDerivedGaugeTimeStamp)
* [getDifferenceMode()](/Java/CounterMonitor/getDifferenceMode)
* [getInitThreshold()](/Java/CounterMonitor/getInitThreshold)
* [getModulus()](/Java/CounterMonitor/getModulus)
* [getNotificationInfo()](/Java/CounterMonitor/getNotificationInfo)
* [getNotify()](/Java/CounterMonitor/getNotify)
* [getOffset()](/Java/CounterMonitor/getOffset)
* [getThreshold()](/Java/CounterMonitor/getThreshold)
* [setDifferenceMode()](/Java/CounterMonitor/setDifferenceMode)
* [setInitThreshold()](/Java/CounterMonitor/setInitThreshold)
* [setModulus()](/Java/CounterMonitor/setModulus)
* [setNotify()](/Java/CounterMonitor/setNotify)
* [setOffset()](/Java/CounterMonitor/setOffset)
* [setThreshold()](/Java/CounterMonitor/setThreshold)
* [start()](/Java/CounterMonitor/start)
* [stop()](/Java/CounterMonitor/stop)

## Ejemplo
~~~java
{{ site.data.Java.C.CounterMonitor.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CounterMonitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
