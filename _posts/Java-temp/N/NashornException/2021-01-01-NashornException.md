---
title: NashornException
permalink: /Java/NashornException/
date: 2021-01-11
key: Java.N.NashornException
category: Java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NashornException.description }}

## Sintaxis
~~~java
public abstract class NashornException extends RuntimeException
~~~

## Constructores
* [NashornException()](/Java/NashornException/NashornException/)

## Métodos
* [getColumnNumber()](/Java/NashornException/getColumnNumber)
* [getEcmaError()](/Java/NashornException/getEcmaError)
* [getFileName()](/Java/NashornException/getFileName)
* [getLineNumber()](/Java/NashornException/getLineNumber)
* [getScriptFrames()](/Java/NashornException/getScriptFrames)
* [getScriptStackString()](/Java/NashornException/getScriptStackString)
* [getThrown()](/Java/NashornException/getThrown)
* [setColumnNumber()](/Java/NashornException/setColumnNumber)
* [setEcmaError()](/Java/NashornException/setEcmaError)
* [setFileName()](/Java/NashornException/setFileName)
* [setLineNumber()](/Java/NashornException/setLineNumber)

## Ejemplo
~~~java
{{ site.data.Java.N.NashornException.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NashornException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
