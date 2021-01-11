---
title: EventListenerProxy
permalink: Java/EventListenerProxy
date: 2021-01-11
key: JavaJava.E.EventListenerProxy
category: java
tags: ['java se', 'java.util', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EventListenerProxy.description }}

## Sintaxis
~~~java
public abstract class EventListenerProxy<T extends EventListener> extends Object implements EventListener
~~~

## Constructores
* [EventListenerProxy()](/Java/EventListenerProxy/EventListenerProxy/)

## Métodos
* [getListener()](/Java/EventListenerProxy/getListener)

## Ejemplo
~~~java
{{ site.data.Java.E.EventListenerProxy.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventListenerProxy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
