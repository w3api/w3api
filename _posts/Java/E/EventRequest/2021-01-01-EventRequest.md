---
title: EventRequest
permalink: /Java/EventRequest/
date: 2021-01-11
key: Java.E.EventRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EventRequest.description }}

## Sintaxis
~~~java
public interface EventRequest extends Mirror
~~~

## Campos
* [SUSPEND_ALL](/Java/EventRequest/SUSPEND_ALL)
* [SUSPEND_EVENT_THREAD](/Java/EventRequest/SUSPEND_EVENT_THREAD)
* [SUSPEND_NONE](/Java/EventRequest/SUSPEND_NONE)

## Métodos
* [addCountFilter()](/Java/EventRequest/addCountFilter)
* [disable()](/Java/EventRequest/disable)
* [enable()](/Java/EventRequest/enable)
* [getProperty()](/Java/EventRequest/getProperty)
* [isEnabled()](/Java/EventRequest/isEnabled)
* [putProperty()](/Java/EventRequest/putProperty)
* [setEnabled()](/Java/EventRequest/setEnabled)
* [setSuspendPolicy()](/Java/EventRequest/setSuspendPolicy)
* [suspendPolicy()](/Java/EventRequest/suspendPolicy)

## Ejemplo
~~~java
{{ site.data.Java.E.EventRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
