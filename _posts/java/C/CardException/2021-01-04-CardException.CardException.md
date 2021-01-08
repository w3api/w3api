---
title: CardException.CardException()
permalink: Java/CardException/CardException
date: 2021-01-04
key: JavaJava.C.CardException
category: java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardException.constructores valor="CardException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CardException(String message)
public CardException(String message, Throwable cause)
public CardException(Throwable cause)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[CardException](/Java/CardException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CardException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
