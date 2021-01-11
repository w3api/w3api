---
title: HotSpotDiagnosticMXBean
permalink: Java/HotSpotDiagnosticMXBean
date: 2021-01-11
key: JavaJava.H.HotSpotDiagnosticMXBean
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HotSpotDiagnosticMXBean.description }}

## Sintaxis
~~~java
public interface HotSpotDiagnosticMXBean extends PlatformManagedObject
~~~

## Métodos
* [dumpHeap()](/Java/HotSpotDiagnosticMXBean/dumpHeap)
* [getDiagnosticOptions()](/Java/HotSpotDiagnosticMXBean/getDiagnosticOptions)
* [getVMOption()](/Java/HotSpotDiagnosticMXBean/getVMOption)
* [setVMOption()](/Java/HotSpotDiagnosticMXBean/setVMOption)

## Ejemplo
~~~java
{{ site.data.Java.H.HotSpotDiagnosticMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HotSpotDiagnosticMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
