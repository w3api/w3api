---
title: ClassPrepareRequest
permalink: Java/ClassPrepareRequest
date: 2021-01-11
key: JavaJava.C.ClassPrepareRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassPrepareRequest.description }}

## Sintaxis
~~~java
public interface ClassPrepareRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/ClassPrepareRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/ClassPrepareRequest/addClassFilter)
* [addSourceNameFilter()](/Java/ClassPrepareRequest/addSourceNameFilter)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassPrepareRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassPrepareRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
