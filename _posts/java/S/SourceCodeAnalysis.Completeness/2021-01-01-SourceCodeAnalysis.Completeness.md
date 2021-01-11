---
title: SourceCodeAnalysis.Completeness
permalink: Java/SourceCodeAnalysis/Completeness
date: 2021-01-11
key: JavaJava.S.SourceCodeAnalysis.Completeness
category: java
tags: ['java se', 'jdk.jshell', 'jdk.jshell', 'enumerado java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SourceCodeAnalysis.Completeness.description }}

## Sintaxis
~~~java
public static enum SourceCodeAnalysis.Completeness extends Enum<SourceCodeAnalysis.Completeness>
~~~

## Enumerados
* [COMPLETE](/Java/SourceCodeAnalysis/Completeness/COMPLETE)
* [COMPLETE_WITH_SEMI](/Java/SourceCodeAnalysis/Completeness/COMPLETE_WITH_SEMI)
* [CONSIDERED_INCOMPLETE](/Java/SourceCodeAnalysis/Completeness/CONSIDERED_INCOMPLETE)
* [DEFINITELY_INCOMPLETE](/Java/SourceCodeAnalysis/Completeness/DEFINITELY_INCOMPLETE)
* [EMPTY](/Java/SourceCodeAnalysis/Completeness/EMPTY)
* [UNKNOWN](/Java/SourceCodeAnalysis/Completeness/UNKNOWN)

## Métodos
* [isComplete()](/Java/SourceCodeAnalysis/Completeness/isComplete)
* [valueOf()](/Java/SourceCodeAnalysis/Completeness/valueOf)
* [values()](/Java/SourceCodeAnalysis/Completeness/values)

## Ejemplo
~~~java
{{ site.data.Java.S.SourceCodeAnalysis.Completeness.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SourceCodeAnalysis.Completeness.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
