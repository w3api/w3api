---
title: TimerTask
permalink: Java/TimerTask
date: 2021-01-11
key: JavaJava.T.TimerTask
category: java
tags: ['java se', 'java.util', 'java.base', 'clase java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TimerTask.description }}

## Sintaxis
~~~java
public abstract class TimerTask extends Object implements Runnable
~~~

## Constructores
* [TimerTask()](/Java/TimerTask/TimerTask/)

## Métodos
* [cancel()](/Java/TimerTask/cancel)
* [run()](/Java/TimerTask/run)
* [scheduledExecutionTime()](/Java/TimerTask/scheduledExecutionTime)

## Ejemplo
~~~java
{{ site.data.Java.T.TimerTask.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TimerTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
