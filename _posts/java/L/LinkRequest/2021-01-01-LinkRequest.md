---
title: LinkRequest
permalink: Java/LinkRequest
date: 2021-01-11
key: JavaJava.L.LinkRequest
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LinkRequest.description }}

## Sintaxis
~~~java
public interface LinkRequest
~~~

## Métodos
* [getArguments()](/Java/LinkRequest/getArguments)
* [getCallSiteDescriptor()](/Java/LinkRequest/getCallSiteDescriptor)
* [getReceiver()](/Java/LinkRequest/getReceiver)
* [isCallSiteUnstable()](/Java/LinkRequest/isCallSiteUnstable)
* [replaceArguments()](/Java/LinkRequest/replaceArguments)

## Ejemplo
~~~java
{{ site.data.Java.L.LinkRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
