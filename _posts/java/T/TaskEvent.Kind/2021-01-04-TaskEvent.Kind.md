---
title: TaskEvent.Kind
permalink: Java/TaskEvent/Kind
date: 2021-01-04
key: JavaJava.T.TaskEvent.Kind
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TaskEvent.Kind.description }}

## Sintaxis
~~~java
public static enum TaskEvent.Kind extends Enum<TaskEvent.Kind>
~~~

## Enumerados
* [ANALYZE](/Java/TaskEvent/Kind/ANALYZE)
* [ANNOTATION_PROCESSING](/Java/TaskEvent/Kind/ANNOTATION_PROCESSING)
* [ANNOTATION_PROCESSING_ROUND](/Java/TaskEvent/Kind/ANNOTATION_PROCESSING_ROUND)
* [COMPILATION](/Java/TaskEvent/Kind/COMPILATION)
* [ENTER](/Java/TaskEvent/Kind/ENTER)
* [GENERATE](/Java/TaskEvent/Kind/GENERATE)
* [PARSE](/Java/TaskEvent/Kind/PARSE)

## Métodos
* [valueOf()](/Java/TaskEvent/Kind/valueOf)
* [values()](/Java/TaskEvent/Kind/values)

## Ejemplo
~~~java
{{ site.data.Java.T.TaskEvent.Kind.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TaskEvent.Kind.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
