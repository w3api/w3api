---
title: CurrencyNameProvider.getSymbol()
permalink: /Java/CurrencyNameProvider/getSymbol/
date: 2021-01-11
key: Java.C.CurrencyNameProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CurrencyNameProvider.metodos valor="getSymbol" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String getSymbol(String currencyCode, Locale locale)
~~~

## Parámetros
* **String currencyCode**,  {% include w3api/param_description.html metodo=_dato parametro="String currencyCode" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CurrencyNameProvider](/Java/CurrencyNameProvider/)

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
