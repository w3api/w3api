---
title: PolicySpi
permalink: /Java/PolicySpi/
date: 2021-01-11
key: Java.P.PolicySpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PolicySpi.description }}

## Sintaxis
~~~java
public abstract class PolicySpi extends Object
~~~

## Constructores
* [PolicySpi()](/Java/PolicySpi/PolicySpi/)

## Métodos
* [engineGetPermissions()](/Java/PolicySpi/engineGetPermissions/)
* [engineImplies()](/Java/PolicySpi/engineImplies/)
* [engineRefresh()](/Java/PolicySpi/engineRefresh/)

## Ejemplo
~~~java
{{ site.data.Java.P.PolicySpi.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PolicySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
