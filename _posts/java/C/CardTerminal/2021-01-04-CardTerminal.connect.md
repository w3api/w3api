---
title: CardTerminal.connect()
permalink: Java/CardTerminal/connect
date: 2021-01-04
key: JavaJava.C.CardTerminal
category: java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminal.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Card connect(String protocol) throws CardException
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}

## Excepciones
[CardException](/Java/CardException/), [SecurityException](/Java/SecurityException/), [CardNotPresentException](/Java/CardNotPresentException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
