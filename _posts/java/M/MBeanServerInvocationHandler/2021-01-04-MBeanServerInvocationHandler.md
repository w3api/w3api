---
title: MBeanServerInvocationHandler
permalink: Java/MBeanServerInvocationHandler
date: 2021-01-04
key: JavaJava.M.MBeanServerInvocationHandler
category: java
tags: ['java se', 'javax.management', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MBeanServerInvocationHandler.description }}

## Sintaxis
~~~java
public class MBeanServerInvocationHandler extends Object implements InvocationHandler
~~~

## Constructores
* [MBeanServerInvocationHandler()](/Java/MBeanServerInvocationHandler/MBeanServerInvocationHandler/)

## Métodos
* [getMBeanServerConnection()](/Java/MBeanServerInvocationHandler/getMBeanServerConnection)
* [getObjectName()](/Java/MBeanServerInvocationHandler/getObjectName)
* [isMXBean()](/Java/MBeanServerInvocationHandler/isMXBean)
* [newProxyInstance()](/Java/MBeanServerInvocationHandler/newProxyInstance)

## Ejemplo
~~~java
{{ site.data.Java.M.MBeanServerInvocationHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerInvocationHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
