---
title: JobStateReasons
permalink: Java/JobStateReasons
date: 2021-01-04
key: JavaJava.J.JobStateReasons
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JobStateReasons.description }}

## Sintaxis
~~~java
public final class JobStateReasons extends HashSet<JobStateReason> implements PrintJobAttribute
~~~

## Constructores
* [JobStateReasons()](/Java/JobStateReasons/JobStateReasons/)

## Métodos
* [add()](/Java/JobStateReasons/add)
* [getCategory()](/Java/JobStateReasons/getCategory)
* [getName()](/Java/JobStateReasons/getName)

## Ejemplo
~~~java
{{ site.data.Java.J.JobStateReasons.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JobStateReasons.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
