---
title: MemoryManagerMXBean
permalink: /Java/MemoryManagerMXBean/
date: 2021-01-11
key: Java.M.MemoryManagerMXBean
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemoryManagerMXBean.description }}

## Sintaxis
~~~java
public interface MemoryManagerMXBean extends PlatformManagedObject
~~~

## Métodos
* [getMemoryPoolNames()](/Java/MemoryManagerMXBean/getMemoryPoolNames)
* [getName()](/Java/MemoryManagerMXBean/getName)
* [isValid()](/Java/MemoryManagerMXBean/isValid)

## Ejemplo
~~~java
{{ site.data.Java.M.MemoryManagerMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryManagerMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
