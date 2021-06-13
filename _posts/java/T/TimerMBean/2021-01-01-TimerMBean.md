---
title: TimerMBean
permalink: /Java/TimerMBean/
date: 2021-01-11
key: Java.T.TimerMBean
category: Java
tags: ['java se', 'javax.management.timer', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TimerMBean.description }}

## Sintaxis
~~~java
public interface TimerMBean
~~~

## Métodos
* [addNotification()](/Java/TimerMBean/addNotification)
* [getAllNotificationIDs()](/Java/TimerMBean/getAllNotificationIDs)
* [getDate()](/Java/TimerMBean/getDate)
* [getFixedRate()](/Java/TimerMBean/getFixedRate)
* [getNbNotifications()](/Java/TimerMBean/getNbNotifications)
* [getNbOccurences()](/Java/TimerMBean/getNbOccurences)
* [getNotificationIDs()](/Java/TimerMBean/getNotificationIDs)
* [getNotificationMessage()](/Java/TimerMBean/getNotificationMessage)
* [getNotificationType()](/Java/TimerMBean/getNotificationType)
* [getNotificationUserData()](/Java/TimerMBean/getNotificationUserData)
* [getPeriod()](/Java/TimerMBean/getPeriod)
* [getSendPastNotifications()](/Java/TimerMBean/getSendPastNotifications)
* [isActive()](/Java/TimerMBean/isActive)
* [isEmpty()](/Java/TimerMBean/isEmpty)
* [removeAllNotifications()](/Java/TimerMBean/removeAllNotifications)
* [removeNotification()](/Java/TimerMBean/removeNotification)
* [removeNotifications()](/Java/TimerMBean/removeNotifications)
* [setSendPastNotifications()](/Java/TimerMBean/setSendPastNotifications)
* [start()](/Java/TimerMBean/start)
* [stop()](/Java/TimerMBean/stop)

## Ejemplo
~~~java
{{ site.data.Java.T.TimerMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TimerMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
