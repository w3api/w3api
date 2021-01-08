---
title: MonitorWaitRequest
permalink: Java/MonitorWaitRequest
date: 2021-01-04
key: JavaJava.M.MonitorWaitRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorWaitRequest.description }}

## Sintaxis
~~~java
public interface MonitorWaitRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/MonitorWaitRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/MonitorWaitRequest/addClassFilter)
* [addInstanceFilter()](/Java/MonitorWaitRequest/addInstanceFilter)
* [addThreadFilter()](/Java/MonitorWaitRequest/addThreadFilter)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorWaitRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorWaitRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
