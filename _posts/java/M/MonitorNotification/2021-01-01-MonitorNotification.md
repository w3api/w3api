---
title: MonitorNotification
permalink: Java/MonitorNotification
date: 2021-01-11
key: JavaJava.M.MonitorNotification
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorNotification.description }}

## Sintaxis
~~~java
public class MonitorNotification extends Notification
~~~

## Campos
* [OBSERVED_ATTRIBUTE_ERROR](/Java/MonitorNotification/OBSERVED_ATTRIBUTE_ERROR)
* [OBSERVED_ATTRIBUTE_TYPE_ERROR](/Java/MonitorNotification/OBSERVED_ATTRIBUTE_TYPE_ERROR)
* [OBSERVED_OBJECT_ERROR](/Java/MonitorNotification/OBSERVED_OBJECT_ERROR)
* [RUNTIME_ERROR](/Java/MonitorNotification/RUNTIME_ERROR)
* [STRING_TO_COMPARE_VALUE_DIFFERED](/Java/MonitorNotification/STRING_TO_COMPARE_VALUE_DIFFERED)
* [STRING_TO_COMPARE_VALUE_MATCHED](/Java/MonitorNotification/STRING_TO_COMPARE_VALUE_MATCHED)
* [THRESHOLD_ERROR](/Java/MonitorNotification/THRESHOLD_ERROR)
* [THRESHOLD_HIGH_VALUE_EXCEEDED](/Java/MonitorNotification/THRESHOLD_HIGH_VALUE_EXCEEDED)
* [THRESHOLD_LOW_VALUE_EXCEEDED](/Java/MonitorNotification/THRESHOLD_LOW_VALUE_EXCEEDED)
* [THRESHOLD_VALUE_EXCEEDED](/Java/MonitorNotification/THRESHOLD_VALUE_EXCEEDED)

## Métodos
* [getDerivedGauge()](/Java/MonitorNotification/getDerivedGauge)
* [getObservedAttribute()](/Java/MonitorNotification/getObservedAttribute)
* [getObservedObject()](/Java/MonitorNotification/getObservedObject)
* [getTrigger()](/Java/MonitorNotification/getTrigger)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorNotification.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
