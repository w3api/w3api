---
title: CardTerminals.list()
permalink: /Java/CardTerminals/list/
date: 2021-01-11
key: Java.C.CardTerminals
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminals.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public List<CardTerminal> list() throws CardException
public abstract List<CardTerminal> list(CardTerminals.State state) throws CardException
~~~

## Parámetros
* **CardTerminals.State state**,  {% include w3api/param_description.html metodo=_dato parametro="CardTerminals.State state" %}

## Excepciones
[CardException](/Java/CardException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CardTerminals](/Java/CardTerminals/)

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
