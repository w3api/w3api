---
title: RMIConnection
permalink: Java/RMIConnection
date: 2021-01-11
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RMIConnection.description }}

## Sintaxis
~~~java
public interface RMIConnection extends Closeable, Remote
~~~

## Métodos
* [addNotificationListener()](/Java/RMIConnection/addNotificationListener)
* [addNotificationListeners()](/Java/RMIConnection/addNotificationListeners)
* [close()](/Java/RMIConnection/close)
* [createMBean()](/Java/RMIConnection/createMBean)
* [fetchNotifications()](/Java/RMIConnection/fetchNotifications)
* [getAttribute()](/Java/RMIConnection/getAttribute)
* [getAttributes()](/Java/RMIConnection/getAttributes)
* [getConnectionId()](/Java/RMIConnection/getConnectionId)
* [getDefaultDomain()](/Java/RMIConnection/getDefaultDomain)
* [getDomains()](/Java/RMIConnection/getDomains)
* [getMBeanCount()](/Java/RMIConnection/getMBeanCount)
* [getMBeanInfo()](/Java/RMIConnection/getMBeanInfo)
* [getObjectInstance()](/Java/RMIConnection/getObjectInstance)
* [invoke()](/Java/RMIConnection/invoke)
* [isInstanceOf()](/Java/RMIConnection/isInstanceOf)
* [isRegistered()](/Java/RMIConnection/isRegistered)
* [queryMBeans()](/Java/RMIConnection/queryMBeans)
* [queryNames()](/Java/RMIConnection/queryNames)
* [removeNotificationListener()](/Java/RMIConnection/removeNotificationListener)
* [removeNotificationListeners()](/Java/RMIConnection/removeNotificationListeners)
* [setAttribute()](/Java/RMIConnection/setAttribute)
* [setAttributes()](/Java/RMIConnection/setAttributes)
* [unregisterMBean()](/Java/RMIConnection/unregisterMBean)

## Ejemplo
~~~java
{{ site.data.Java.R.RMIConnection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
