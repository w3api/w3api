---
title: PlatformLoggingMXBean
permalink: Java/PlatformLoggingMXBean
date: 2021-01-04
key: JavaJava.P.PlatformLoggingMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PlatformLoggingMXBean.description }}

## Sintaxis
~~~java
public interface PlatformLoggingMXBean extends PlatformManagedObject
~~~

## Métodos
* [getLoggerLevel()](/Java/PlatformLoggingMXBean/getLoggerLevel)
* [getLoggerNames()](/Java/PlatformLoggingMXBean/getLoggerNames)
* [getParentLoggerName()](/Java/PlatformLoggingMXBean/getParentLoggerName)
* [setLoggerLevel()](/Java/PlatformLoggingMXBean/setLoggerLevel)

## Ejemplo
~~~java
{{ site.data.Java.P.PlatformLoggingMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PlatformLoggingMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
