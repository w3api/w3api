---
title: ScheduledExecutorService
permalink: /Java/ScheduledExecutorService/
date: 2021-01-11
key: Java.S.ScheduledExecutorService
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ScheduledExecutorService.description }}

## Sintaxis
~~~java
public interface ScheduledExecutorService extends ExecutorService
~~~

## Métodos
* [schedule()](/Java/ScheduledExecutorService/schedule)
* [scheduleAtFixedRate()](/Java/ScheduledExecutorService/scheduleAtFixedRate)
* [scheduleWithFixedDelay()](/Java/ScheduledExecutorService/scheduleWithFixedDelay)

## Ejemplo
~~~java
{{ site.data.Java.S.ScheduledExecutorService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScheduledExecutorService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
