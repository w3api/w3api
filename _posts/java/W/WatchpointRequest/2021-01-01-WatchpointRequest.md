---
title: WatchpointRequest
permalink: Java/WatchpointRequest
date: 2021-01-11
key: JavaJava.W.WatchpointRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WatchpointRequest.description }}

## Sintaxis
~~~java
public interface WatchpointRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/WatchpointRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/WatchpointRequest/addClassFilter)
* [addInstanceFilter()](/Java/WatchpointRequest/addInstanceFilter)
* [addThreadFilter()](/Java/WatchpointRequest/addThreadFilter)
* [field()](/Java/WatchpointRequest/field)

## Ejemplo
~~~java
{{ site.data.Java.W.WatchpointRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WatchpointRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
