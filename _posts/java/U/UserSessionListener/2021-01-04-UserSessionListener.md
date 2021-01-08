---
title: UserSessionListener
permalink: Java/UserSessionListener
date: 2021-01-04
key: JavaJava.U.UserSessionListener
category: java
tags: ['java se', 'java.awt.desktop', 'java.desktop', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UserSessionListener.description }}

## Sintaxis
~~~java
public interface UserSessionListener extends SystemEventListener
~~~

## Métodos
* [userSessionActivated()](/Java/UserSessionListener/userSessionActivated)
* [userSessionDeactivated()](/Java/UserSessionListener/userSessionDeactivated)

## Ejemplo
~~~java
{{ site.data.Java.U.UserSessionListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UserSessionListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
