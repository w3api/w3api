---
title: ClassUnloadRequest
permalink: /Java/ClassUnloadRequest/
date: 2021-01-11
key: Java.C.ClassUnloadRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassUnloadRequest.description }}

## Sintaxis
~~~java
public interface ClassUnloadRequest extends EventRequest
~~~

## Métodos
* [addClassExclusionFilter()](/Java/ClassUnloadRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/ClassUnloadRequest/addClassFilter)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassUnloadRequest.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassUnloadRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
