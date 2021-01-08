---
title: MBeanServerConnection
permalink: Java/MBeanServerConnection
date: 2021-01-04
key: JavaJava.M.MBeanServerConnection
category: java
tags: ['java se', 'javax.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MBeanServerConnection.description }}

## Sintaxis
~~~java
public interface MBeanServerConnection
~~~

## Métodos
* [addNotificationListener()](/Java/MBeanServerConnection/addNotificationListener)
* [createMBean()](/Java/MBeanServerConnection/createMBean)
* [getAttribute()](/Java/MBeanServerConnection/getAttribute)
* [getAttributes()](/Java/MBeanServerConnection/getAttributes)
* [getDefaultDomain()](/Java/MBeanServerConnection/getDefaultDomain)
* [getDomains()](/Java/MBeanServerConnection/getDomains)
* [getMBeanCount()](/Java/MBeanServerConnection/getMBeanCount)
* [getMBeanInfo()](/Java/MBeanServerConnection/getMBeanInfo)
* [getObjectInstance()](/Java/MBeanServerConnection/getObjectInstance)
* [invoke()](/Java/MBeanServerConnection/invoke)
* [isInstanceOf()](/Java/MBeanServerConnection/isInstanceOf)
* [isRegistered()](/Java/MBeanServerConnection/isRegistered)
* [queryMBeans()](/Java/MBeanServerConnection/queryMBeans)
* [queryNames()](/Java/MBeanServerConnection/queryNames)
* [removeNotificationListener()](/Java/MBeanServerConnection/removeNotificationListener)
* [setAttribute()](/Java/MBeanServerConnection/setAttribute)
* [setAttributes()](/Java/MBeanServerConnection/setAttributes)
* [unregisterMBean()](/Java/MBeanServerConnection/unregisterMBean)

## Ejemplo
~~~java
{{ site.data.Java.M.MBeanServerConnection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
