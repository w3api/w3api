---
title: SystemSleepListener
permalink: Java/SystemSleepListener
date: 2021-01-11
key: JavaJava.S.SystemSleepListener
category: java
tags: ['java se', 'java.awt.desktop', 'java.desktop', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SystemSleepListener.description }}

## Sintaxis
~~~java
public interface SystemSleepListener extends SystemEventListener
~~~

## Métodos
* [systemAboutToSleep()](/Java/SystemSleepListener/systemAboutToSleep)
* [systemAwoke()](/Java/SystemSleepListener/systemAwoke)

## Ejemplo
~~~java
{{ site.data.Java.S.SystemSleepListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SystemSleepListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
