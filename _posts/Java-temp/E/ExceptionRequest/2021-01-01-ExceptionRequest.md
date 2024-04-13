---
title: ExceptionRequest
permalink: /Java/ExceptionRequest/
date: 2021-01-11
key: Java.E.ExceptionRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExceptionRequest.description }}

## Sintaxis
~~~java
public interface ExceptionRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/ExceptionRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/ExceptionRequest/addClassFilter)
* [addInstanceFilter()](/Java/ExceptionRequest/addInstanceFilter)
* [addThreadFilter()](/Java/ExceptionRequest/addThreadFilter)
* [exception()](/Java/ExceptionRequest/exception)
* [notifyCaught()](/Java/ExceptionRequest/notifyCaught)
* [notifyUncaught()](/Java/ExceptionRequest/notifyUncaught)

## Ejemplo
~~~java
{{ site.data.Java.E.ExceptionRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExceptionRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
