---
title: ClassLoadingMXBean
permalink: Java/ClassLoadingMXBean
date: 2021-01-11
key: JavaJava.C.ClassLoadingMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassLoadingMXBean.description }}

## Sintaxis
~~~java
public interface ClassLoadingMXBean extends PlatformManagedObject
~~~

## Métodos
* [getLoadedClassCount()](/Java/ClassLoadingMXBean/getLoadedClassCount)
* [getTotalLoadedClassCount()](/Java/ClassLoadingMXBean/getTotalLoadedClassCount)
* [getUnloadedClassCount()](/Java/ClassLoadingMXBean/getUnloadedClassCount)
* [isVerbose()](/Java/ClassLoadingMXBean/isVerbose)
* [setVerbose()](/Java/ClassLoadingMXBean/setVerbose)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassLoadingMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoadingMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
