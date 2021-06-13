---
title: CardTerminal.connect()
permalink: /Java/CardTerminal/connect/
date: 2021-01-11
key: Java.C.CardTerminal
category: Java
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
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}

## Excepciones
[CardException](/Java/CardException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [SecurityException](/Java/SecurityException/), [CardNotPresentException](/Java/CardNotPresentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CardTerminal](/Java/CardTerminal/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
