---
title: CardTerminals.getTerminal()
permalink: /Java/CardTerminals/getTerminal/
date: 2021-01-11
key: Java.C.CardTerminals
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminals.metodos valor="getTerminal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CardTerminal getTerminal(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
