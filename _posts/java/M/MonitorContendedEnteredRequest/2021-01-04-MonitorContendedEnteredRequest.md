---
title: MonitorContendedEnteredRequest
permalink: Java/MonitorContendedEnteredRequest
date: 2021-01-04
key: JavaJava.M.MonitorContendedEnteredRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorContendedEnteredRequest.description }}

## Sintaxis
~~~java
public interface MonitorContendedEnteredRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/MonitorContendedEnteredRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/MonitorContendedEnteredRequest/addClassFilter)
* [addInstanceFilter()](/Java/MonitorContendedEnteredRequest/addInstanceFilter)
* [addThreadFilter()](/Java/MonitorContendedEnteredRequest/addThreadFilter)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorContendedEnteredRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorContendedEnteredRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
