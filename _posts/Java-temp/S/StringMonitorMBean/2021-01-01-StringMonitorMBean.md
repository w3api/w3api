---
title: StringMonitorMBean
permalink: /Java/StringMonitorMBean/
date: 2021-01-11
key: Java.S.StringMonitorMBean
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StringMonitorMBean.description }}

## Sintaxis
~~~java
public interface StringMonitorMBean extends MonitorMBean
~~~

## Métodos
* [getDerivedGauge()](/Java/StringMonitorMBean/getDerivedGauge)
* [getDerivedGaugeTimeStamp()](/Java/StringMonitorMBean/getDerivedGaugeTimeStamp)
* [getNotifyDiffer()](/Java/StringMonitorMBean/getNotifyDiffer)
* [getNotifyMatch()](/Java/StringMonitorMBean/getNotifyMatch)
* [getStringToCompare()](/Java/StringMonitorMBean/getStringToCompare)
* [setNotifyDiffer()](/Java/StringMonitorMBean/setNotifyDiffer)
* [setNotifyMatch()](/Java/StringMonitorMBean/setNotifyMatch)
* [setStringToCompare()](/Java/StringMonitorMBean/setStringToCompare)

## Ejemplo
~~~java
{{ site.data.Java.S.StringMonitorMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringMonitorMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
