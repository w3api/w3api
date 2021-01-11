---
title: ObjectReference
permalink: Java/ObjectReference
date: 2021-01-11
key: JavaJava.O.ObjectReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectReference.description }}

## Sintaxis
~~~java
public interface ObjectReference extends Value
~~~

## Campos
* [INVOKE_NONVIRTUAL](/Java/ObjectReference/INVOKE_NONVIRTUAL)
* [INVOKE_SINGLE_THREADED](/Java/ObjectReference/INVOKE_SINGLE_THREADED)

## Métodos
* [disableCollection()](/Java/ObjectReference/disableCollection)
* [enableCollection()](/Java/ObjectReference/enableCollection)
* [entryCount()](/Java/ObjectReference/entryCount)
* [equals()](/Java/ObjectReference/equals)
* [getValue()](/Java/ObjectReference/getValue)
* [getValues()](/Java/ObjectReference/getValues)
* [hashCode()](/Java/ObjectReference/hashCode)
* [invokeMethod()](/Java/ObjectReference/invokeMethod)
* [isCollected()](/Java/ObjectReference/isCollected)
* [owningThread()](/Java/ObjectReference/owningThread)
* [referenceType()](/Java/ObjectReference/referenceType)
* [referringObjects()](/Java/ObjectReference/referringObjects)
* [setValue()](/Java/ObjectReference/setValue)
* [uniqueID()](/Java/ObjectReference/uniqueID)
* [waitingThreads()](/Java/ObjectReference/waitingThreads)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
