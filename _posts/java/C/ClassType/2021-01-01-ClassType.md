---
title: ClassType
permalink: /Java/ClassType/
date: 2021-01-11
key: Java.C.ClassType
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassType.description }}

## Sintaxis
~~~java
public interface ClassType extends ReferenceType
~~~

## Campos
* [INVOKE_SINGLE_THREADED](/Java/ClassType/INVOKE_SINGLE_THREADED)

## Métodos
* [allInterfaces()](/Java/ClassType/allInterfaces)
* [concreteMethodByName()](/Java/ClassType/concreteMethodByName)
* [interfaces()](/Java/ClassType/interfaces)
* [invokeMethod()](/Java/ClassType/invokeMethod)
* [isEnum()](/Java/ClassType/isEnum)
* [newInstance()](/Java/ClassType/newInstance)
* [setValue()](/Java/ClassType/setValue)
* [subclasses()](/Java/ClassType/subclasses)
* [superclass()](/Java/ClassType/superclass)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassType.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
