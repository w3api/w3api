---
title: SimpleScriptContext
permalink: Java/SimpleScriptContext
date: 2021-01-11
key: JavaJava.S.SimpleScriptContext
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SimpleScriptContext.description }}

## Sintaxis
~~~java
public class SimpleScriptContext extends Object implements ScriptContext
~~~

## Constructores
* [SimpleScriptContext()](/Java/SimpleScriptContext/SimpleScriptContext/)

## Campos
* [engineScope](/Java/SimpleScriptContext/engineScope)
* [errorWriter](/Java/SimpleScriptContext/errorWriter)
* [globalScope](/Java/SimpleScriptContext/globalScope)
* [reader](/Java/SimpleScriptContext/reader)
* [writer](/Java/SimpleScriptContext/writer)

## Métodos
* [getAttribute()](/Java/SimpleScriptContext/getAttribute)
* [getAttributesScope()](/Java/SimpleScriptContext/getAttributesScope)
* [getBindings()](/Java/SimpleScriptContext/getBindings)
* [removeAttribute()](/Java/SimpleScriptContext/removeAttribute)
* [setAttribute()](/Java/SimpleScriptContext/setAttribute)
* [setBindings()](/Java/SimpleScriptContext/setBindings)

## Ejemplo
~~~java
{{ site.data.Java.S.SimpleScriptContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleScriptContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
