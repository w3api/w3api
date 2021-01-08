---
title: GaugeMonitor
permalink: Java/GaugeMonitor
date: 2021-01-04
key: JavaJava.G.GaugeMonitor
category: java
tags: ['java se', 'javax.management.monitor', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.G.GaugeMonitor.description }}

## Sintaxis
~~~java
public class GaugeMonitor extends Monitor implements GaugeMonitorMBean
~~~

## Constructores
* [GaugeMonitor()](/Java/GaugeMonitor/GaugeMonitor/)

## Métodos
* [getDerivedGauge()](/Java/GaugeMonitor/getDerivedGauge)
* [getDerivedGaugeTimeStamp()](/Java/GaugeMonitor/getDerivedGaugeTimeStamp)
* [getDifferenceMode()](/Java/GaugeMonitor/getDifferenceMode)
* [getHighThreshold()](/Java/GaugeMonitor/getHighThreshold)
* [getLowThreshold()](/Java/GaugeMonitor/getLowThreshold)
* [getNotificationInfo()](/Java/GaugeMonitor/getNotificationInfo)
* [getNotifyHigh()](/Java/GaugeMonitor/getNotifyHigh)
* [getNotifyLow()](/Java/GaugeMonitor/getNotifyLow)
* [setDifferenceMode()](/Java/GaugeMonitor/setDifferenceMode)
* [setNotifyHigh()](/Java/GaugeMonitor/setNotifyHigh)
* [setNotifyLow()](/Java/GaugeMonitor/setNotifyLow)
* [setThresholds()](/Java/GaugeMonitor/setThresholds)
* [start()](/Java/GaugeMonitor/start)
* [stop()](/Java/GaugeMonitor/stop)

## Ejemplo
~~~java
{{ site.data.Java.G.GaugeMonitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GaugeMonitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
