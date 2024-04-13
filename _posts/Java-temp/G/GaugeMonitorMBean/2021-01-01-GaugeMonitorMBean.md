---
title: GaugeMonitorMBean
permalink: /Java/GaugeMonitorMBean/
date: 2021-01-11
key: Java.G.GaugeMonitorMBean
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.G.GaugeMonitorMBean.description }}

## Sintaxis
~~~java
public interface GaugeMonitorMBean extends MonitorMBean
~~~

## Métodos
* [getDerivedGauge()](/Java/GaugeMonitorMBean/getDerivedGauge)
* [getDerivedGaugeTimeStamp()](/Java/GaugeMonitorMBean/getDerivedGaugeTimeStamp)
* [getDifferenceMode()](/Java/GaugeMonitorMBean/getDifferenceMode)
* [getHighThreshold()](/Java/GaugeMonitorMBean/getHighThreshold)
* [getLowThreshold()](/Java/GaugeMonitorMBean/getLowThreshold)
* [getNotifyHigh()](/Java/GaugeMonitorMBean/getNotifyHigh)
* [getNotifyLow()](/Java/GaugeMonitorMBean/getNotifyLow)
* [setDifferenceMode()](/Java/GaugeMonitorMBean/setDifferenceMode)
* [setNotifyHigh()](/Java/GaugeMonitorMBean/setNotifyHigh)
* [setNotifyLow()](/Java/GaugeMonitorMBean/setNotifyLow)
* [setThresholds()](/Java/GaugeMonitorMBean/setThresholds)

## Ejemplo
~~~java
{{ site.data.Java.G.GaugeMonitorMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GaugeMonitorMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
