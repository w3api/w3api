---
title: MBeanServer
permalink: Java/MBeanServer
date: 2021-01-11
key: JavaJava.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MBeanServer.description }}

## Sintaxis
~~~java
public interface MBeanServer extends MBeanServerConnection
~~~

## Métodos
* [addNotificationListener()](/Java/MBeanServer/addNotificationListener)
* [createMBean()](/Java/MBeanServer/createMBean)
* [deserialize()](/Java/MBeanServer/deserialize)
* [getAttribute()](/Java/MBeanServer/getAttribute)
* [getAttributes()](/Java/MBeanServer/getAttributes)
* [getClassLoader()](/Java/MBeanServer/getClassLoader)
* [getClassLoaderFor()](/Java/MBeanServer/getClassLoaderFor)
* [getClassLoaderRepository()](/Java/MBeanServer/getClassLoaderRepository)
* [getMBeanCount()](/Java/MBeanServer/getMBeanCount)
* [instantiate()](/Java/MBeanServer/instantiate)
* [isRegistered()](/Java/MBeanServer/isRegistered)
* [queryMBeans()](/Java/MBeanServer/queryMBeans)
* [queryNames()](/Java/MBeanServer/queryNames)
* [registerMBean()](/Java/MBeanServer/registerMBean)
* [setAttribute()](/Java/MBeanServer/setAttribute)
* [setAttributes()](/Java/MBeanServer/setAttributes)
* [unregisterMBean()](/Java/MBeanServer/unregisterMBean)

## Ejemplo
~~~java
{{ site.data.Java.M.MBeanServer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
