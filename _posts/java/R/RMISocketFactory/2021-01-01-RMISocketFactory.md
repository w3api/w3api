---
title: RMISocketFactory
permalink: Java/RMISocketFactory
date: 2021-01-11
key: Java.R.RMISocketFactory
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RMISocketFactory.description }}

## Sintaxis
~~~java
public abstract class RMISocketFactory extends Object implements RMIClientSocketFactory, RMIServerSocketFactory
~~~

## Constructores
* [RMISocketFactory()](/Java/RMISocketFactory/RMISocketFactory/)

## Métodos
* [createServerSocket()](/Java/RMISocketFactory/createServerSocket)
* [createSocket()](/Java/RMISocketFactory/createSocket)
* [getDefaultSocketFactory()](/Java/RMISocketFactory/getDefaultSocketFactory)
* [getFailureHandler()](/Java/RMISocketFactory/getFailureHandler)
* [getSocketFactory()](/Java/RMISocketFactory/getSocketFactory)
* [setFailureHandler()](/Java/RMISocketFactory/setFailureHandler)
* [setSocketFactory()](/Java/RMISocketFactory/setSocketFactory)

## Ejemplo
~~~java
{{ site.data.Java.R.RMISocketFactory.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMISocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
