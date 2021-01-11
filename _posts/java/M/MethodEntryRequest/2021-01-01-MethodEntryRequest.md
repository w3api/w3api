---
title: MethodEntryRequest
permalink: Java/MethodEntryRequest
date: 2021-01-11
key: JavaJava.M.MethodEntryRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MethodEntryRequest.description }}

## Sintaxis
~~~java
public interface MethodEntryRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/MethodEntryRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/MethodEntryRequest/addClassFilter)
* [addInstanceFilter()](/Java/MethodEntryRequest/addInstanceFilter)
* [addThreadFilter()](/Java/MethodEntryRequest/addThreadFilter)

## Ejemplo
~~~java
{{ site.data.Java.M.MethodEntryRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodEntryRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
