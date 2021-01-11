---
title: InitialContext
permalink: Java/InitialContext
date: 2021-01-11
key: JavaJava.I.InitialContext
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'clase java', 'Java 1.3', 'JNDI Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.InitialContext.description }}

## Sintaxis
~~~java
public class InitialContext extends Object implements Context
~~~

## Constructores
* [InitialContext()](/Java/InitialContext/InitialContext/)

## Campos
* [defaultInitCtx](/Java/InitialContext/defaultInitCtx)
* [gotDefault](/Java/InitialContext/gotDefault)
* [myProps](/Java/InitialContext/myProps)

## Métodos
* [composeName()](/Java/InitialContext/composeName)
* [doLookup()](/Java/InitialContext/doLookup)
* [getDefaultInitCtx()](/Java/InitialContext/getDefaultInitCtx)
* [getURLOrDefaultInitCtx()](/Java/InitialContext/getURLOrDefaultInitCtx)
* [init()](/Java/InitialContext/init)

## Ejemplo
~~~java
{{ site.data.Java.I.InitialContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InitialContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
