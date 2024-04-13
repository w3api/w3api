---
title: PolicyNode
permalink: /Java/PolicyNode/
date: 2021-01-11
key: Java.P.PolicyNode
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PolicyNode.description }}

## Sintaxis
~~~java
public interface PolicyNode
~~~

## Métodos
* [getChildren()](/Java/PolicyNode/getChildren/)
* [getDepth()](/Java/PolicyNode/getDepth/)
* [getExpectedPolicies()](/Java/PolicyNode/getExpectedPolicies/)
* [getParent()](/Java/PolicyNode/getParent/)
* [getPolicyQualifiers()](/Java/PolicyNode/getPolicyQualifiers/)
* [getValidPolicy()](/Java/PolicyNode/getValidPolicy/)
* [isCritical()](/Java/PolicyNode/isCritical/)

## Ejemplo
~~~java
{{ site.data.Java.P.PolicyNode.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PolicyNode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
