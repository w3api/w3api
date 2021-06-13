---
title: RuntimeMXBean
permalink: Java/RuntimeMXBean
date: 2021-01-11
key: Java.R.RuntimeMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RuntimeMXBean.description }}

## Sintaxis
~~~java
public interface RuntimeMXBean extends PlatformManagedObject
~~~

## Métodos
* [getBootClassPath()](/Java/RuntimeMXBean/getBootClassPath)
* [getClassPath()](/Java/RuntimeMXBean/getClassPath)
* [getInputArguments()](/Java/RuntimeMXBean/getInputArguments)
* [getLibraryPath()](/Java/RuntimeMXBean/getLibraryPath)
* [getManagementSpecVersion()](/Java/RuntimeMXBean/getManagementSpecVersion)
* [getName()](/Java/RuntimeMXBean/getName)
* [getPid()](/Java/RuntimeMXBean/getPid)
* [getSpecName()](/Java/RuntimeMXBean/getSpecName)
* [getSpecVendor()](/Java/RuntimeMXBean/getSpecVendor)
* [getSpecVersion()](/Java/RuntimeMXBean/getSpecVersion)
* [getStartTime()](/Java/RuntimeMXBean/getStartTime)
* [getSystemProperties()](/Java/RuntimeMXBean/getSystemProperties)
* [getUptime()](/Java/RuntimeMXBean/getUptime)
* [getVmName()](/Java/RuntimeMXBean/getVmName)
* [getVmVendor()](/Java/RuntimeMXBean/getVmVendor)
* [getVmVersion()](/Java/RuntimeMXBean/getVmVersion)
* [isBootClassPathSupported()](/Java/RuntimeMXBean/isBootClassPathSupported)

## Ejemplo
~~~java
{{ site.data.Java.R.RuntimeMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RuntimeMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
