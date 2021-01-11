---
title: MonitorContendedEnterRequest
permalink: Java/MonitorContendedEnterRequest
date: 2021-01-11
key: JavaJava.M.MonitorContendedEnterRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorContendedEnterRequest.description }}

## Sintaxis
~~~java
public interface MonitorContendedEnterRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/MonitorContendedEnterRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/MonitorContendedEnterRequest/addClassFilter)
* [addInstanceFilter()](/Java/MonitorContendedEnterRequest/addInstanceFilter)
* [addThreadFilter()](/Java/MonitorContendedEnterRequest/addThreadFilter)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorContendedEnterRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorContendedEnterRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
