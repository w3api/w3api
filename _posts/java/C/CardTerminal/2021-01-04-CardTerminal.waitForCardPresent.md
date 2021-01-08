---
title: CardTerminal.waitForCardPresent()
permalink: Java/CardTerminal/waitForCardPresent
date: 2021-01-04
key: JavaJava.C.CardTerminal
category: java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminal.metodos valor="waitForCardPresent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean waitForCardPresent(long timeout) throws CardException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[CardException](/Java/CardException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CardTerminal](/Java/CardTerminal/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CardTerminal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
