---
title: RequiredModelMBean
permalink: Java/RequiredModelMBean
date: 2021-01-04
key: JavaJava.R.RequiredModelMBean
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RequiredModelMBean.description }}

## Sintaxis
~~~java
public class RequiredModelMBean extends Object implements ModelMBean, MBeanRegistration, NotificationEmitter
~~~

## Constructores
* [RequiredModelMBean()](/Java/RequiredModelMBean/RequiredModelMBean/)

## Métodos
* [addNotificationListener()](/Java/RequiredModelMBean/addNotificationListener)
* [getAttribute()](/Java/RequiredModelMBean/getAttribute)
* [getAttributes()](/Java/RequiredModelMBean/getAttributes)
* [getClassLoaderRepository()](/Java/RequiredModelMBean/getClassLoaderRepository)
* [getMBeanInfo()](/Java/RequiredModelMBean/getMBeanInfo)
* [getNotificationInfo()](/Java/RequiredModelMBean/getNotificationInfo)
* [invoke()](/Java/RequiredModelMBean/invoke)
* [load()](/Java/RequiredModelMBean/load)
* [postDeregister()](/Java/RequiredModelMBean/postDeregister)
* [postRegister()](/Java/RequiredModelMBean/postRegister)
* [preDeregister()](/Java/RequiredModelMBean/preDeregister)
* [preRegister()](/Java/RequiredModelMBean/preRegister)
* [removeNotificationListener()](/Java/RequiredModelMBean/removeNotificationListener)
* [setAttribute()](/Java/RequiredModelMBean/setAttribute)
* [setAttributes()](/Java/RequiredModelMBean/setAttributes)
* [setManagedResource()](/Java/RequiredModelMBean/setManagedResource)
* [setModelMBeanInfo()](/Java/RequiredModelMBean/setModelMBeanInfo)
* [store()](/Java/RequiredModelMBean/store)

## Ejemplo
~~~java
{{ site.data.Java.R.RequiredModelMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RequiredModelMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
