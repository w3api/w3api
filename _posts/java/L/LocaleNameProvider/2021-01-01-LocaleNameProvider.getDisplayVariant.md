---
title: LocaleNameProvider.getDisplayVariant()
permalink: Java/LocaleNameProvider/getDisplayVariant
date: 2021-01-11
key: Java.L.LocaleNameProvider
category: java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocaleNameProvider.metodos valor="getDisplayVariant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String getDisplayVariant(String variant, Locale locale)
~~~

## Parámetros
* **String variant**,  {% include w3api/param_description.html metodo=_dato parametro="String variant" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LocaleNameProvider](/Java/LocaleNameProvider/)

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
