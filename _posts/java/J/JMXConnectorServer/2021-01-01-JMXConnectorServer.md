---
title: JMXConnectorServer
permalink: Java/JMXConnectorServer
date: 2021-01-11
key: JavaJava.J.JMXConnectorServer
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JMXConnectorServer.description }}

## Sintaxis
~~~java
public abstract class JMXConnectorServer extends NotificationBroadcasterSupport implements JMXConnectorServerMBean, MBeanRegistration, JMXAddressable
~~~

## Constructores
* [JMXConnectorServer()](/Java/JMXConnectorServer/JMXConnectorServer/)

## Campos
* [AUTHENTICATOR](/Java/JMXConnectorServer/AUTHENTICATOR)

## Métodos
* [connectionClosed()](/Java/JMXConnectorServer/connectionClosed)
* [connectionFailed()](/Java/JMXConnectorServer/connectionFailed)
* [connectionOpened()](/Java/JMXConnectorServer/connectionOpened)
* [getMBeanServer()](/Java/JMXConnectorServer/getMBeanServer)
* [getNotificationInfo()](/Java/JMXConnectorServer/getNotificationInfo)
* [preDeregister()](/Java/JMXConnectorServer/preDeregister)
* [preRegister()](/Java/JMXConnectorServer/preRegister)
* [toJMXConnector()](/Java/JMXConnectorServer/toJMXConnector)

## Ejemplo
~~~java
{{ site.data.Java.J.JMXConnectorServer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnectorServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
