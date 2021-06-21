---
title: CardTerminal
permalink: /Java/CardTerminal/
date: 2021-01-11
key: Java.C.CardTerminal
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CardTerminal.description }}

## Sintaxis
~~~java
public abstract class CardTerminal extends Object
~~~

## Constructores
* [CardTerminal()](/Java/CardTerminal/CardTerminal/)

## Métodos
* [connect()](/Java/CardTerminal/connect)
* [getName()](/Java/CardTerminal/getName)
* [isCardPresent()](/Java/CardTerminal/isCardPresent)
* [waitForCardAbsent()](/Java/CardTerminal/waitForCardAbsent)
* [waitForCardPresent()](/Java/CardTerminal/waitForCardPresent)

## Ejemplo
~~~java
{{ site.data.Java.C.CardTerminal.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CardTerminal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
