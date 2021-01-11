---
title: UnixOperatingSystemMXBean
permalink: Java/UnixOperatingSystemMXBean
date: 2021-01-11
key: JavaJava.U.UnixOperatingSystemMXBean
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UnixOperatingSystemMXBean.description }}

## Sintaxis
~~~java
public interface UnixOperatingSystemMXBean extends OperatingSystemMXBean
~~~

## Métodos
* [getMaxFileDescriptorCount()](/Java/UnixOperatingSystemMXBean/getMaxFileDescriptorCount)
* [getOpenFileDescriptorCount()](/Java/UnixOperatingSystemMXBean/getOpenFileDescriptorCount)

## Ejemplo
~~~java
{{ site.data.Java.U.UnixOperatingSystemMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UnixOperatingSystemMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
