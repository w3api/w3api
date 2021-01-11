---
title: JobSheets
permalink: Java/JobSheets
date: 2021-01-11
key: JavaJava.J.JobSheets
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JobSheets.description }}

## Sintaxis
~~~java
public class JobSheets extends EnumSyntax implements PrintRequestAttribute, PrintJobAttribute
~~~

## Constructores
* [JobSheets()](/Java/JobSheets/JobSheets/)

## Campos
* [NONE](/Java/JobSheets/NONE)
* [STANDARD](/Java/JobSheets/STANDARD)

## Métodos
* [getCategory()](/Java/JobSheets/getCategory)
* [getEnumValueTable()](/Java/JobSheets/getEnumValueTable)
* [getName()](/Java/JobSheets/getName)
* [getStringTable()](/Java/JobSheets/getStringTable)

## Ejemplo
~~~java
{{ site.data.Java.J.JobSheets.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JobSheets.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
