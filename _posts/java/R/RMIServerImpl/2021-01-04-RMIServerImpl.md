---
title: RMIServerImpl
permalink: Java/RMIServerImpl
date: 2021-01-04
key: JavaJava.R.RMIServerImpl
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RMIServerImpl.description }}

## Sintaxis
~~~java
public abstract class RMIServerImpl extends Object implements Closeable, RMIServer
~~~

## Constructores
* [RMIServerImpl()](/Java/RMIServerImpl/RMIServerImpl/)

## Métodos
* [clientClosed()](/Java/RMIServerImpl/clientClosed)
* [close()](/Java/RMIServerImpl/close)
* [closeClient()](/Java/RMIServerImpl/closeClient)
* [closeServer()](/Java/RMIServerImpl/closeServer)
* [export()](/Java/RMIServerImpl/export)
* [getDefaultClassLoader()](/Java/RMIServerImpl/getDefaultClassLoader)
* [getMBeanServer()](/Java/RMIServerImpl/getMBeanServer)
* [getProtocol()](/Java/RMIServerImpl/getProtocol)
* [makeClient()](/Java/RMIServerImpl/makeClient)
* [newClient()](/Java/RMIServerImpl/newClient)
* [setDefaultClassLoader()](/Java/RMIServerImpl/setDefaultClassLoader)
* [setMBeanServer()](/Java/RMIServerImpl/setMBeanServer)
* [toStub()](/Java/RMIServerImpl/toStub)

## Ejemplo
~~~java
{{ site.data.Java.R.RMIServerImpl.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIServerImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
