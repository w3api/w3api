---
title: Processor
permalink: Java/Processor
date: 2021-01-04
key: JavaJava.P.Processor
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.Processor.description }}

## Sintaxis
~~~java
public interface Processor
~~~

## Métodos
* [getCompletions()](/Java/Processor/getCompletions)
* [getSupportedAnnotationTypes()](/Java/Processor/getSupportedAnnotationTypes)
* [getSupportedOptions()](/Java/Processor/getSupportedOptions)
* [getSupportedSourceVersion()](/Java/Processor/getSupportedSourceVersion)
* [init()](/Java/Processor/init)
* [process()](/Java/Processor/process)

## Ejemplo
~~~java
{{ site.data.Java.P.Processor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Processor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
