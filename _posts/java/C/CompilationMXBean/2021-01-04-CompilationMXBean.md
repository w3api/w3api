---
title: CompilationMXBean
permalink: Java/CompilationMXBean
date: 2021-01-04
key: JavaJava.C.CompilationMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompilationMXBean.description }}

## Sintaxis
~~~java
public interface CompilationMXBean extends PlatformManagedObject
~~~

## Métodos
* [getName()](/Java/CompilationMXBean/getName)
* [getTotalCompilationTime()](/Java/CompilationMXBean/getTotalCompilationTime)
* [isCompilationTimeMonitoringSupported()](/Java/CompilationMXBean/isCompilationTimeMonitoringSupported)

## Ejemplo
~~~java
{{ site.data.Java.C.CompilationMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompilationMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
