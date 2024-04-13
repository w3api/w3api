---
title: PersistenceDelegate
permalink: /Java/PersistenceDelegate/
date: 2021-01-11
key: Java.P.PersistenceDelegate
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PersistenceDelegate.description }}

## Sintaxis
~~~java
public abstract class PersistenceDelegate extends Object
~~~

## Constructores
* [PersistenceDelegate()](/Java/PersistenceDelegate/PersistenceDelegate/)

## Métodos
* [initialize()](/Java/PersistenceDelegate/initialize)
* [instantiate()](/Java/PersistenceDelegate/instantiate)
* [mutatesTo()](/Java/PersistenceDelegate/mutatesTo)
* [writeObject()](/Java/PersistenceDelegate/writeObject)

## Ejemplo
~~~java
{{ site.data.Java.P.PersistenceDelegate.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PersistenceDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
