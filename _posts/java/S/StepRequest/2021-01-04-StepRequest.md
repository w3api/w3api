---
title: StepRequest
permalink: Java/StepRequest
date: 2021-01-04
key: JavaJava.S.StepRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StepRequest.description }}

## Sintaxis
~~~java
public interface StepRequest extends EventRequest
~~~

## Campos
* [STEP_INTO](/Java/StepRequest/STEP_INTO)
* [STEP_LINE](/Java/StepRequest/STEP_LINE)
* [STEP_MIN](/Java/StepRequest/STEP_MIN)
* [STEP_OUT](/Java/StepRequest/STEP_OUT)
* [STEP_OVER](/Java/StepRequest/STEP_OVER)

## Métodos
* [addClassExclusionFilter()](/Java/StepRequest/addClassExclusionFilter)
* [addClassFilter()](/Java/StepRequest/addClassFilter)
* [addInstanceFilter()](/Java/StepRequest/addInstanceFilter)
* [depth()](/Java/StepRequest/depth)
* [size()](/Java/StepRequest/size)
* [thread()](/Java/StepRequest/thread)

## Ejemplo
~~~java
{{ site.data.Java.S.StepRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StepRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
