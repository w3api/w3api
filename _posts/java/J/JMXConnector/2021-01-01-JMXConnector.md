---
title: JMXConnector
permalink: Java/JMXConnector
date: 2021-01-11
key: JavaJava.J.JMXConnector
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JMXConnector.description }}

## Sintaxis
~~~java
public interface JMXConnector extends Closeable
~~~

## Campos
* [CREDENTIALS](/Java/JMXConnector/CREDENTIALS)

## Métodos
* [addConnectionNotificationListener()](/Java/JMXConnector/addConnectionNotificationListener)
* [close()](/Java/JMXConnector/close)
* [connect()](/Java/JMXConnector/connect)
* [getConnectionId()](/Java/JMXConnector/getConnectionId)
* [getMBeanServerConnection()](/Java/JMXConnector/getMBeanServerConnection)
* [removeConnectionNotificationListener()](/Java/JMXConnector/removeConnectionNotificationListener)

## Ejemplo
~~~java
{{ site.data.Java.J.JMXConnector.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
