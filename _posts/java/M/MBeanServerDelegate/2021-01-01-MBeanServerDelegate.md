---
title: MBeanServerDelegate
permalink: Java/MBeanServerDelegate
date: 2021-01-11
key: JavaJava.M.MBeanServerDelegate
category: Java
tags: ['java se', 'javax.management', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MBeanServerDelegate.description }}

## Sintaxis
~~~java
public class MBeanServerDelegate extends Object implements MBeanServerDelegateMBean, NotificationEmitter
~~~

## Constructores
* [MBeanServerDelegate()](/Java/MBeanServerDelegate/MBeanServerDelegate/)

## Campos
* [DELEGATE_NAME](/Java/MBeanServerDelegate/DELEGATE_NAME)

## Métodos
* [getImplementationName()](/Java/MBeanServerDelegate/getImplementationName)
* [getImplementationVendor()](/Java/MBeanServerDelegate/getImplementationVendor)
* [getImplementationVersion()](/Java/MBeanServerDelegate/getImplementationVersion)
* [getMBeanServerId()](/Java/MBeanServerDelegate/getMBeanServerId)
* [getSpecificationName()](/Java/MBeanServerDelegate/getSpecificationName)
* [getSpecificationVendor()](/Java/MBeanServerDelegate/getSpecificationVendor)
* [getSpecificationVersion()](/Java/MBeanServerDelegate/getSpecificationVersion)
* [sendNotification()](/Java/MBeanServerDelegate/sendNotification)

## Ejemplo
~~~java
{{ site.data.Java.M.MBeanServerDelegate.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
