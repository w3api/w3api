---
title: RecordedStackTrace
permalink: /Java/RecordedStackTrace/
date: 2021-01-11
key: Java.R.RecordedStackTrace
category: Java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecordedStackTrace.description }}

## Sintaxis
~~~java
public final class RecordedStackTrace extends RecordedObject
~~~

## Métodos
* [getFrames()](/Java/RecordedStackTrace/getFrames)
* [isTruncated()](/Java/RecordedStackTrace/isTruncated)

## Ejemplo
~~~java
{{ site.data.Java.R.RecordedStackTrace.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecordedStackTrace.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
