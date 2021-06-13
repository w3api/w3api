---
title: MemoryMXBean
permalink: Java/MemoryMXBean
date: 2021-01-11
key: JavaJava.M.MemoryMXBean
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemoryMXBean.description }}

## Sintaxis
~~~java
public interface MemoryMXBean extends PlatformManagedObject
~~~

## Métodos
* [gc()](/Java/MemoryMXBean/gc)
* [getHeapMemoryUsage()](/Java/MemoryMXBean/getHeapMemoryUsage)
* [getNonHeapMemoryUsage()](/Java/MemoryMXBean/getNonHeapMemoryUsage)
* [getObjectPendingFinalizationCount()](/Java/MemoryMXBean/getObjectPendingFinalizationCount)
* [isVerbose()](/Java/MemoryMXBean/isVerbose)
* [setVerbose()](/Java/MemoryMXBean/setVerbose)

## Ejemplo
~~~java
{{ site.data.Java.M.MemoryMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
