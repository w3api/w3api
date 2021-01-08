---
title: NamingEvent
permalink: Java/NamingEvent
date: 2021-01-04
key: JavaJava.N.NamingEvent
category: java
tags: ['java se', 'javax.naming.event', 'java.naming', 'clase java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NamingEvent.description }}

## Sintaxis
~~~java
public class NamingEvent extends EventObject
~~~

## Constructores
* [NamingEvent()](/Java/NamingEvent/NamingEvent/)

## Campos
* [changeInfo](/Java/NamingEvent/changeInfo)
* [newBinding](/Java/NamingEvent/newBinding)
* [OBJECT_ADDED](/Java/NamingEvent/OBJECT_ADDED)
* [OBJECT_CHANGED](/Java/NamingEvent/OBJECT_CHANGED)
* [OBJECT_REMOVED](/Java/NamingEvent/OBJECT_REMOVED)
* [OBJECT_RENAMED](/Java/NamingEvent/OBJECT_RENAMED)
* [oldBinding](/Java/NamingEvent/oldBinding)
* [type](/Java/NamingEvent/type)

## Métodos
* [dispatch()](/Java/NamingEvent/dispatch)
* [getChangeInfo()](/Java/NamingEvent/getChangeInfo)
* [getEventContext()](/Java/NamingEvent/getEventContext)
* [getNewBinding()](/Java/NamingEvent/getNewBinding)
* [getOldBinding()](/Java/NamingEvent/getOldBinding)
* [getType()](/Java/NamingEvent/getType)

## Ejemplo
~~~java
{{ site.data.Java.N.NamingEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NamingEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
