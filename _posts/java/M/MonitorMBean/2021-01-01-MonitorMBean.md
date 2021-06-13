---
title: MonitorMBean
permalink: Java/MonitorMBean
date: 2021-01-11
key: JavaJava.M.MonitorMBean
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorMBean.description }}

## Sintaxis
~~~java
public interface MonitorMBean
~~~

## Métodos
* [addObservedObject()](/Java/MonitorMBean/addObservedObject)
* [containsObservedObject()](/Java/MonitorMBean/containsObservedObject)
* [getGranularityPeriod()](/Java/MonitorMBean/getGranularityPeriod)
* [getObservedAttribute()](/Java/MonitorMBean/getObservedAttribute)
* [getObservedObject()](/Java/MonitorMBean/getObservedObject)
* [getObservedObjects()](/Java/MonitorMBean/getObservedObjects)
* [isActive()](/Java/MonitorMBean/isActive)
* [removeObservedObject()](/Java/MonitorMBean/removeObservedObject)
* [setGranularityPeriod()](/Java/MonitorMBean/setGranularityPeriod)
* [setObservedAttribute()](/Java/MonitorMBean/setObservedAttribute)
* [setObservedObject()](/Java/MonitorMBean/setObservedObject)
* [start()](/Java/MonitorMBean/start)
* [stop()](/Java/MonitorMBean/stop)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
