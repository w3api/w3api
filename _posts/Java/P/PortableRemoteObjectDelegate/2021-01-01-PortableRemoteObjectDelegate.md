---
title: PortableRemoteObjectDelegate
permalink: /Java/PortableRemoteObjectDelegate/
date: 2021-01-11
key: Java.P.PortableRemoteObjectDelegate
category: Java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PortableRemoteObjectDelegate.description }}

## Sintaxis
~~~java
public interface PortableRemoteObjectDelegate
~~~

## Métodos
* [connect()](/Java/PortableRemoteObjectDelegate/connect)
* [exportObject()](/Java/PortableRemoteObjectDelegate/exportObject)
* [narrow()](/Java/PortableRemoteObjectDelegate/narrow)
* [toStub()](/Java/PortableRemoteObjectDelegate/toStub)
* [unexportObject()](/Java/PortableRemoteObjectDelegate/unexportObject)

## Ejemplo
~~~java
{{ site.data.Java.P.PortableRemoteObjectDelegate.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PortableRemoteObjectDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
