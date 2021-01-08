---
title: MethodExitRequest
permalink: Java/MethodExitRequest
date: 2021-01-04
key: JavaJava.M.MethodExitRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MethodExitRequest.description }}

## Sintaxis
~~~java
public interface MethodExitRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/MethodExitRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/MethodExitRequest/addClassFilter)
* [addInstanceFilter()](/Java/MethodExitRequest/addInstanceFilter)
* [addThreadFilter()](/Java/MethodExitRequest/addThreadFilter)

## Ejemplo
~~~java
{{ site.data.Java.M.MethodExitRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodExitRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
