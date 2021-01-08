---
title: ScriptEngine
permalink: Java/ScriptEngine
date: 2021-01-04
key: JavaJava.S.ScriptEngine
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ScriptEngine.description }}

## Sintaxis
~~~java
public interface ScriptEngine
~~~

## Campos
* [ARGV](/Java/ScriptEngine/ARGV)
* [ENGINE](/Java/ScriptEngine/ENGINE)
* [ENGINE_VERSION](/Java/ScriptEngine/ENGINE_VERSION)
* [FILENAME](/Java/ScriptEngine/FILENAME)
* [LANGUAGE](/Java/ScriptEngine/LANGUAGE)
* [LANGUAGE_VERSION](/Java/ScriptEngine/LANGUAGE_VERSION)
* [NAME](/Java/ScriptEngine/NAME)

## Métodos
* [createBindings()](/Java/ScriptEngine/createBindings)
* [eval()](/Java/ScriptEngine/eval)
* [get()](/Java/ScriptEngine/get)
* [getBindings()](/Java/ScriptEngine/getBindings)
* [getContext()](/Java/ScriptEngine/getContext)
* [getFactory()](/Java/ScriptEngine/getFactory)
* [put()](/Java/ScriptEngine/put)
* [setBindings()](/Java/ScriptEngine/setBindings)
* [setContext()](/Java/ScriptEngine/setContext)

## Ejemplo
~~~java
{{ site.data.Java.S.ScriptEngine.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScriptEngine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
