---
title: MemoryPoolMXBean
permalink: Java/MemoryPoolMXBean
date: 2021-01-11
key: JavaJava.M.MemoryPoolMXBean
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemoryPoolMXBean.description }}

## Sintaxis
~~~java
public interface MemoryPoolMXBean extends PlatformManagedObject
~~~

## Métodos
* [getCollectionUsage()](/Java/MemoryPoolMXBean/getCollectionUsage)
* [getCollectionUsageThreshold()](/Java/MemoryPoolMXBean/getCollectionUsageThreshold)
* [getCollectionUsageThresholdCount()](/Java/MemoryPoolMXBean/getCollectionUsageThresholdCount)
* [getMemoryManagerNames()](/Java/MemoryPoolMXBean/getMemoryManagerNames)
* [getName()](/Java/MemoryPoolMXBean/getName)
* [getPeakUsage()](/Java/MemoryPoolMXBean/getPeakUsage)
* [getType()](/Java/MemoryPoolMXBean/getType)
* [getUsage()](/Java/MemoryPoolMXBean/getUsage)
* [getUsageThreshold()](/Java/MemoryPoolMXBean/getUsageThreshold)
* [getUsageThresholdCount()](/Java/MemoryPoolMXBean/getUsageThresholdCount)
* [isCollectionUsageThresholdExceeded()](/Java/MemoryPoolMXBean/isCollectionUsageThresholdExceeded)
* [isCollectionUsageThresholdSupported()](/Java/MemoryPoolMXBean/isCollectionUsageThresholdSupported)
* [isUsageThresholdExceeded()](/Java/MemoryPoolMXBean/isUsageThresholdExceeded)
* [isUsageThresholdSupported()](/Java/MemoryPoolMXBean/isUsageThresholdSupported)
* [isValid()](/Java/MemoryPoolMXBean/isValid)
* [resetPeakUsage()](/Java/MemoryPoolMXBean/resetPeakUsage)
* [setCollectionUsageThreshold()](/Java/MemoryPoolMXBean/setCollectionUsageThreshold)
* [setUsageThreshold()](/Java/MemoryPoolMXBean/setUsageThreshold)

## Ejemplo
~~~java
{{ site.data.Java.M.MemoryPoolMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryPoolMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
