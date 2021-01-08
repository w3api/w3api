---
title: HierarchyEvent
permalink: Java/HierarchyEvent
date: 2021-01-04
key: JavaJava.H.HierarchyEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'clase java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HierarchyEvent.description }}

## Sintaxis
~~~java
public class HierarchyEvent extends AWTEvent
~~~

## Constructores
* [HierarchyEvent()](/Java/HierarchyEvent/HierarchyEvent/)

## Campos
* [ANCESTOR_MOVED](/Java/HierarchyEvent/ANCESTOR_MOVED)
* [ANCESTOR_RESIZED](/Java/HierarchyEvent/ANCESTOR_RESIZED)
* [DISPLAYABILITY_CHANGED](/Java/HierarchyEvent/DISPLAYABILITY_CHANGED)
* [HIERARCHY_CHANGED](/Java/HierarchyEvent/HIERARCHY_CHANGED)
* [HIERARCHY_FIRST](/Java/HierarchyEvent/HIERARCHY_FIRST)
* [HIERARCHY_LAST](/Java/HierarchyEvent/HIERARCHY_LAST)
* [PARENT_CHANGED](/Java/HierarchyEvent/PARENT_CHANGED)
* [SHOWING_CHANGED](/Java/HierarchyEvent/SHOWING_CHANGED)

## Métodos
* [getChanged()](/Java/HierarchyEvent/getChanged)
* [getChangedParent()](/Java/HierarchyEvent/getChangedParent)
* [getChangeFlags()](/Java/HierarchyEvent/getChangeFlags)
* [getComponent()](/Java/HierarchyEvent/getComponent)
* [paramString()](/Java/HierarchyEvent/paramString)

## Ejemplo
~~~java
{{ site.data.Java.H.HierarchyEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HierarchyEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
