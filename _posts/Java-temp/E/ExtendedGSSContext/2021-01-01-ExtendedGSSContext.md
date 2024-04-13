---
title: ExtendedGSSContext
permalink: /Java/ExtendedGSSContext/
date: 2021-01-11
key: Java.E.ExtendedGSSContext
category: Java
tags: ['java se', 'com.sun.security.jgss', 'jdk.security.jgss', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExtendedGSSContext.description }}

## Sintaxis
~~~java
public interface ExtendedGSSContext extends GSSContext
~~~

## Métodos
* [getDelegPolicyState()](/Java/ExtendedGSSContext/getDelegPolicyState)
* [inquireSecContext()](/Java/ExtendedGSSContext/inquireSecContext)
* [requestDelegPolicy()](/Java/ExtendedGSSContext/requestDelegPolicy)

## Ejemplo
~~~java
{{ site.data.Java.E.ExtendedGSSContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExtendedGSSContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
