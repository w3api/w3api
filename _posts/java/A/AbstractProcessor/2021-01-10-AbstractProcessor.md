---
title: AbstractProcessor
permalink: Java/AbstractProcessor
date: 2021-01-10
key: JavaJava.A.AbstractProcessor
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractProcessor.description }}

## Sintaxis
~~~java
public abstract class AbstractProcessor extends Object implements Processor
~~~

## Constructores
* [AbstractProcessor()](/Java/AbstractProcessor/AbstractProcessor/)

## Campos
* [processingEnv](/Java/AbstractProcessor/processingEnv)

## Métodos
* [getCompletions()](/Java/AbstractProcessor/getCompletions)
* [getSupportedAnnotationTypes()](/Java/AbstractProcessor/getSupportedAnnotationTypes)
* [getSupportedOptions()](/Java/AbstractProcessor/getSupportedOptions)
* [getSupportedSourceVersion()](/Java/AbstractProcessor/getSupportedSourceVersion)
* [init()](/Java/AbstractProcessor/init)
* [isInitialized()](/Java/AbstractProcessor/isInitialized)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractProcessor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractProcessor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
