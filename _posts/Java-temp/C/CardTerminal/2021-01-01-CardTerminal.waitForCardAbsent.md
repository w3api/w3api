---
title: CardTerminal.waitForCardAbsent()
permalink: /Java/CardTerminal/waitForCardAbsent/
date: 2021-01-11
key: Java.C.CardTerminal
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminal.metodos valor="waitForCardAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean waitForCardAbsent(long timeout) throws CardException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}

## Excepciones
[CardException](/Java/CardException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
