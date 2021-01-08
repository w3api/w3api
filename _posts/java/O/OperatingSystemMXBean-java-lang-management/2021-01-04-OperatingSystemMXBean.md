---
title: OperatingSystemMXBean
permalink: Java/OperatingSystemMXBean-java-lang-management
date: 2021-01-04
key: JavaJava.O.OperatingSystemMXBean-java-lang-management
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.OperatingSystemMXBean-java-lang-management.description }}

## Sintaxis
~~~java
public interface OperatingSystemMXBean extends PlatformManagedObject
~~~

## Métodos
* [getArch()](/Java/OperatingSystemMXBean-java-lang-management/getArch)
* [getAvailableProcessors()](/Java/OperatingSystemMXBean-java-lang-management/getAvailableProcessors)
* [getName()](/Java/OperatingSystemMXBean-java-lang-management/getName)
* [getSystemLoadAverage()](/Java/OperatingSystemMXBean-java-lang-management/getSystemLoadAverage)
* [getVersion()](/Java/OperatingSystemMXBean-java-lang-management/getVersion)

## Ejemplo
~~~java
{{ site.data.Java.O.OperatingSystemMXBean-java-lang-management.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OperatingSystemMXBean-java-lang-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
