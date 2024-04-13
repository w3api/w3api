---
title: ThreadGroupReference
permalink: /Java/ThreadGroupReference/
date: 2021-01-11
key: Java.T.ThreadGroupReference
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadGroupReference.description }}

## Sintaxis
~~~java
public interface ThreadGroupReference extends ObjectReference
~~~

## Métodos
* [name()](/Java/ThreadGroupReference/name)
* [parent()](/Java/ThreadGroupReference/parent)
* [resume()](/Java/ThreadGroupReference/resume)
* [suspend()](/Java/ThreadGroupReference/suspend)
* [threadGroups()](/Java/ThreadGroupReference/threadGroups)
* [threads()](/Java/ThreadGroupReference/threads)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadGroupReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadGroupReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
