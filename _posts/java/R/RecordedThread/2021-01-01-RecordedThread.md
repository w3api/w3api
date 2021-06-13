---
title: RecordedThread
permalink: Java/RecordedThread
date: 2021-01-11
key: Java.R.RecordedThread
category: java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecordedThread.description }}

## Sintaxis
~~~java
public final class RecordedThread extends RecordedObject
~~~

## Métodos
* [getId()](/Java/RecordedThread/getId)
* [getJavaName()](/Java/RecordedThread/getJavaName)
* [getJavaThreadId()](/Java/RecordedThread/getJavaThreadId)
* [getOSName()](/Java/RecordedThread/getOSName)
* [getOSThreadId()](/Java/RecordedThread/getOSThreadId)
* [getThreadGroup()](/Java/RecordedThread/getThreadGroup)

## Ejemplo
~~~java
{{ site.data.Java.R.RecordedThread.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecordedThread.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
