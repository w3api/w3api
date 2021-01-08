---
title: ThreadMXBean
permalink: Java/ThreadMXBean-com-sun-management
date: 2021-01-04
key: JavaJava.T.ThreadMXBean-com-sun-management
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'interface java', '6u25']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadMXBean-com-sun-management.description }}

## Sintaxis
~~~java
public interface ThreadMXBean extends ThreadMXBean
~~~

## Métodos
* [getThreadAllocatedBytes()](/Java/ThreadMXBean-com-sun-management/getThreadAllocatedBytes)
* [getThreadCpuTime()](/Java/ThreadMXBean-com-sun-management/getThreadCpuTime)
* [getThreadUserTime()](/Java/ThreadMXBean-com-sun-management/getThreadUserTime)
* [isThreadAllocatedMemoryEnabled()](/Java/ThreadMXBean-com-sun-management/isThreadAllocatedMemoryEnabled)
* [isThreadAllocatedMemorySupported()](/Java/ThreadMXBean-com-sun-management/isThreadAllocatedMemorySupported)
* [setThreadAllocatedMemoryEnabled()](/Java/ThreadMXBean-com-sun-management/setThreadAllocatedMemoryEnabled)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadMXBean-com-sun-management.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadMXBean-com-sun-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
