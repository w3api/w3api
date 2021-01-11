---
title: MonitorWaitedRequest
permalink: Java/MonitorWaitedRequest
date: 2021-01-11
key: JavaJava.M.MonitorWaitedRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorWaitedRequest.description }}

## Sintaxis
~~~java
public interface MonitorWaitedRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/MonitorWaitedRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/MonitorWaitedRequest/addClassFilter)
* [addInstanceFilter()](/Java/MonitorWaitedRequest/addInstanceFilter)
* [addThreadFilter()](/Java/MonitorWaitedRequest/addThreadFilter)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorWaitedRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorWaitedRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
