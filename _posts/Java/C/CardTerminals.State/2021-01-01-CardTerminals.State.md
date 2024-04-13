---
title: CardTerminals.State
permalink: /Java/CardTerminals/State/
date: 2021-01-11
key: Java.C.CardTerminals.State
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CardTerminals.State.description }}

## Sintaxis
~~~java
public static enum CardTerminals.State extends Enum<CardTerminals.State>
~~~

## Enumerados
* [ALL](/Java/CardTerminals/State/ALL/)
* [CARD_ABSENT](/Java/CardTerminals/State/CARD_ABSENT/)
* [CARD_INSERTION](/Java/CardTerminals/State/CARD_INSERTION/)
* [CARD_PRESENT](/Java/CardTerminals/State/CARD_PRESENT/)
* [CARD_REMOVAL](/Java/CardTerminals/State/CARD_REMOVAL/)

## Métodos
* [valueOf()](/Java/CardTerminals/State/valueOf/)
* [values()](/Java/CardTerminals/State/values/)

## Ejemplo
~~~java
{{ site.data.Java.C.CardTerminals.State.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CardTerminals.State.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
