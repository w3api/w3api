---
title: BreakpointRequest
permalink: /Java/BreakpointRequest/
date: 2021-01-11
key: Java.B.BreakpointRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BreakpointRequest.description }}

## Sintaxis
~~~java
public interface BreakpointRequest extends EventRequest, Locatable
~~~

## Métodos
* [addInstanceFilter()](/Java/BreakpointRequest/addInstanceFilter)
* [addThreadFilter()](/Java/BreakpointRequest/addThreadFilter)
* [location()](/Java/BreakpointRequest/location)

## Ejemplo
~~~java
{{ site.data.Java.B.BreakpointRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BreakpointRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
