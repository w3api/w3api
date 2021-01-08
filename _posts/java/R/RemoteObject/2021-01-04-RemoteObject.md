---
title: RemoteObject
permalink: Java/RemoteObject
date: 2021-01-04
key: JavaJava.R.RemoteObject
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RemoteObject.description }}

## Sintaxis
~~~java
public abstract class RemoteObject extends Object implements Remote, Serializable
~~~

## Constructores
* [RemoteObject()](/Java/RemoteObject/RemoteObject/)

## Campos
* [ref](/Java/RemoteObject/ref)

## Métodos
* [equals()](/Java/RemoteObject/equals)
* [getRef()](/Java/RemoteObject/getRef)
* [hashCode()](/Java/RemoteObject/hashCode)
* [toString()](/Java/RemoteObject/toString)
* [toStub()](/Java/RemoteObject/toStub)

## Ejemplo
~~~java
{{ site.data.Java.R.RemoteObject.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RemoteObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
