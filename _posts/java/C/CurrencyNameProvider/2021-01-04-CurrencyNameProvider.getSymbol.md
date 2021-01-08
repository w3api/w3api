---
title: CurrencyNameProvider.getSymbol()
permalink: Java/CurrencyNameProvider/getSymbol
date: 2021-01-04
key: JavaJava.C.CurrencyNameProvider
category: java
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
* **String currencyCode**,  {% include w3api/param_description.html metodo=_data parametro="String currencyCode" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CurrencyNameProvider](/Java/CurrencyNameProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CurrencyNameProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
