---
title: MutationEvent
permalink: Java/MutationEvent
date: 2021-01-11
key: JavaJava.M.MutationEvent
category: java
tags: ['java se', 'org.w3c.dom.events', 'java.xml', 'interface java', 'Java 1.5', 'DOM Level 2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MutationEvent.description }}

## Sintaxis
~~~java
public interface MutationEvent extends Event
~~~

## Campos
* [ADDITION](/Java/MutationEvent/ADDITION)
* [MODIFICATION](/Java/MutationEvent/MODIFICATION)
* [REMOVAL](/Java/MutationEvent/REMOVAL)

## Métodos
* [getAttrChange()](/Java/MutationEvent/getAttrChange)
* [getAttrName()](/Java/MutationEvent/getAttrName)
* [getNewValue()](/Java/MutationEvent/getNewValue)
* [getPrevValue()](/Java/MutationEvent/getPrevValue)
* [getRelatedNode()](/Java/MutationEvent/getRelatedNode)
* [initMutationEvent()](/Java/MutationEvent/initMutationEvent)

## Ejemplo
~~~java
{{ site.data.Java.M.MutationEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MutationEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
