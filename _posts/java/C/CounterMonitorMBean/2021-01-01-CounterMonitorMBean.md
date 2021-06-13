---
title: CounterMonitorMBean
permalink: /Java/CounterMonitorMBean/
date: 2021-01-11
key: Java.C.CounterMonitorMBean
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CounterMonitorMBean.description }}

## Sintaxis
~~~java
public interface CounterMonitorMBean extends MonitorMBean
~~~

## Métodos
* [getDerivedGauge()](/Java/CounterMonitorMBean/getDerivedGauge)
* [getDerivedGaugeTimeStamp()](/Java/CounterMonitorMBean/getDerivedGaugeTimeStamp)
* [getDifferenceMode()](/Java/CounterMonitorMBean/getDifferenceMode)
* [getInitThreshold()](/Java/CounterMonitorMBean/getInitThreshold)
* [getModulus()](/Java/CounterMonitorMBean/getModulus)
* [getNotify()](/Java/CounterMonitorMBean/getNotify)
* [getOffset()](/Java/CounterMonitorMBean/getOffset)
* [getThreshold()](/Java/CounterMonitorMBean/getThreshold)
* [setDifferenceMode()](/Java/CounterMonitorMBean/setDifferenceMode)
* [setInitThreshold()](/Java/CounterMonitorMBean/setInitThreshold)
* [setModulus()](/Java/CounterMonitorMBean/setModulus)
* [setNotify()](/Java/CounterMonitorMBean/setNotify)
* [setOffset()](/Java/CounterMonitorMBean/setOffset)
* [setThreshold()](/Java/CounterMonitorMBean/setThreshold)

## Ejemplo
~~~java
{{ site.data.Java.C.CounterMonitorMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CounterMonitorMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
