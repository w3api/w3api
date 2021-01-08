---
title: InvocationEvent
permalink: Java/InvocationEvent
date: 2021-01-04
key: JavaJava.I.InvocationEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.InvocationEvent.description }}

## Sintaxis
~~~java
public class InvocationEvent extends AWTEvent implements ActiveEvent
~~~

## Constructores
* [InvocationEvent()](/Java/InvocationEvent/InvocationEvent/)

## Campos
* [catchExceptions](/Java/InvocationEvent/catchExceptions)
* [INVOCATION_DEFAULT](/Java/InvocationEvent/INVOCATION_DEFAULT)
* [INVOCATION_FIRST](/Java/InvocationEvent/INVOCATION_FIRST)
* [INVOCATION_LAST](/Java/InvocationEvent/INVOCATION_LAST)
* [notifier](/Java/InvocationEvent/notifier)
* [runnable](/Java/InvocationEvent/runnable)

## Métodos
* [dispatch()](/Java/InvocationEvent/dispatch)
* [getException()](/Java/InvocationEvent/getException)
* [getThrowable()](/Java/InvocationEvent/getThrowable)
* [getWhen()](/Java/InvocationEvent/getWhen)
* [isDispatched()](/Java/InvocationEvent/isDispatched)
* [paramString()](/Java/InvocationEvent/paramString)

## Ejemplo
~~~java
{{ site.data.Java.I.InvocationEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InvocationEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
