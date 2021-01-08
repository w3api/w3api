---
title: SystemResourcePressureMXBean
permalink: Java/SystemResourcePressureMXBean
date: 2021-01-04
key: JavaJava.S.SystemResourcePressureMXBean
category: java
tags: ['java se', 'jdk.management.cmm', 'jdk.management.cmm', 'interface java', '8u40']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SystemResourcePressureMXBean.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public interface SystemResourcePressureMXBean extends PlatformManagedObject
~~~

## Métodos
* [getMemoryPressure()](/Java/SystemResourcePressureMXBean/getMemoryPressure)
* [setMemoryPressure()](/Java/SystemResourcePressureMXBean/setMemoryPressure)

## Ejemplo
~~~java
{{ site.data.Java.S.SystemResourcePressureMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SystemResourcePressureMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
