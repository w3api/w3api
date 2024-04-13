---
title: CardTerminal.isCardPresent()
permalink: /Java/CardTerminal/isCardPresent/
date: 2021-01-11
key: Java.C.CardTerminal
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminal.metodos valor="isCardPresent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean isCardPresent() throws CardException
~~~

## Excepciones
[CardException](/Java/CardException/)

## Clase Padre
[CardTerminal](/Java/CardTerminal/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
