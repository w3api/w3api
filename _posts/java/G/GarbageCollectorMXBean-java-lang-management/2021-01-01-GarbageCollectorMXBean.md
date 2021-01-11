---
title: GarbageCollectorMXBean
permalink: Java/GarbageCollectorMXBean-java-lang-management
date: 2021-01-11
key: JavaJava.G.GarbageCollectorMXBean-java-lang-management
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.G.GarbageCollectorMXBean-java-lang-management.description }}

## Sintaxis
~~~java
public interface GarbageCollectorMXBean extends MemoryManagerMXBean
~~~

## Métodos
* [getCollectionCount()](/Java/GarbageCollectorMXBean-java-lang-management/getCollectionCount)
* [getCollectionTime()](/Java/GarbageCollectorMXBean-java-lang-management/getCollectionTime)

## Ejemplo
~~~java
{{ site.data.Java.G.GarbageCollectorMXBean-java-lang-management.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GarbageCollectorMXBean-java-lang-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
