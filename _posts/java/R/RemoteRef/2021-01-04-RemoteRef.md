---
title: RemoteRef
permalink: Java/RemoteRef
date: 2021-01-04
key: JavaJava.R.RemoteRef
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RemoteRef.description }}

## Sintaxis
~~~java
public interface RemoteRef extends Externalizable
~~~

## Campos
* [packagePrefix](/Java/RemoteRef/packagePrefix)
* [serialVersionUID](/Java/RemoteRef/serialVersionUID)

## Métodos
* [done()](/Java/RemoteRef/done)
* [getRefClass()](/Java/RemoteRef/getRefClass)
* [invoke()](/Java/RemoteRef/invoke)
* [newCall()](/Java/RemoteRef/newCall)
* [remoteEquals()](/Java/RemoteRef/remoteEquals)
* [remoteHashCode()](/Java/RemoteRef/remoteHashCode)
* [remoteToString()](/Java/RemoteRef/remoteToString)

## Ejemplo
~~~java
{{ site.data.Java.R.RemoteRef.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RemoteRef.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
